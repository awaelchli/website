from django.core import mail
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import get_template

from subscription.models import NewsletterSubscription


def notify_subscribers(sender, instance, **kwargs):
    if instance.first_published_at != instance.last_published_at:
        # Do not send a notification if this is a revision.
        return

    plaintext = get_template('subscription/newsletter/email.txt')
    htmly = get_template('subscription/newsletter/email.html')
    context = {}
    text_content = plaintext.render(context)
    html_content = htmly.render(context)

    recipients = NewsletterSubscription.objects.values_list('email', flat=True)
    connection = mail.get_connection()
    connection.open()
    messages = []
    for recipient in recipients:
        message = mail.EmailMultiAlternatives(
            subject='Hello',
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient],
            connection=connection,
        )
        message.attach_alternative(html_content, "text/html")
        messages.append(message)

    connection.send_messages(messages)
    connection.close()
