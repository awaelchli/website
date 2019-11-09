import telegram
from django.core import mail
from django.conf import settings
from django.template.loader import get_template
from telegram import ParseMode

from settings.models import Subscription
from subscription.models import NewsletterSubscription, SubscriptionPage


def notify_subscribers(sender, instance, **kwargs):
    if instance.first_published_at == instance.last_published_at:
        notify_newsletter_subscribers(instance)
        notify_telegram_channel(instance)


def notify_newsletter_subscribers(instance):
    connection = mail.get_connection()
    connection.open()
    subscription_settings = Subscription.for_site(instance.get_site())
    recipients = NewsletterSubscription.objects.all()
    subject = subscription_settings.email_subject
    subscription_page = subscription_settings.subscription_page
    messages = []
    for recipient in recipients:
        plaintext = get_template('subscription/message/email.txt')
        html = get_template('subscription/message/email.html')
        if subscription_page:
            unsubscribe_url = subscription_page.specific.get_unsubscribe_url_for(recipient)
        else:
            unsubscribe_url = None
        context = {
            'unsubscribe_url': unsubscribe_url
        }
        text_content = plaintext.render(context)
        html_content = html.render(context)

        message = mail.EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient.email],
            connection=connection,
        )
        message.attach_alternative(html_content, "text/html")
        messages.append(message)

    connection.send_messages(messages)
    connection.close()


def notify_telegram_channel(instance):
    subscription_settings = Subscription.for_site(instance.get_site())
    bot_token = subscription_settings.telegram_bot_token
    channel_id = subscription_settings.telegram_channel_id

    if not (bot_token and channel_id):
        return

    message = get_template('subscription/message/telegram.html')
    message = message.render(
        context={
            'post': instance
        }
    )

    bot = telegram.Bot(token=bot_token)
    bot.send_message(
        chat_id=channel_id,
        text=message,
        parse_mode=ParseMode.HTML
    )
