from django import template

from core.forms import NewsletterSubscriptionForm

register = template.Library()


@register.simple_tag()
def get_newsletter_form():
    form = NewsletterSubscriptionForm()
    return form
