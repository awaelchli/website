from django.core import mail
from django.conf import settings
from django.template.loader import get_template

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
    subscription_page = subscription_settings.subscription_page.specific
    messages = []
    for recipient in recipients:
        plaintext = get_template('subscription/newsletter/email.txt')
        html = get_template('subscription/newsletter/email.html')
        context = {
            'unsubscribe_url': subscription_page.get_unsubscribe_url_for(recipient)
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
    pass
