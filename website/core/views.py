from django.views.generic import CreateView

from core.forms import NewsletterSubscriptionForm
from core.models import NewsletterSubscription


class NewsletterSubscriptionView(CreateView):
    model = NewsletterSubscription
    form_class = NewsletterSubscriptionForm
    template_name = 'other/newsletter_form.html'
