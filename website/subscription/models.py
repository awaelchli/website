from django.db import models
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from core.models import BannerPage


class SubscriptionPage(BannerPage):
    template = 'subscription/main.html'
    subpage_types = []
    parent_page_type = [
        'home.HomePage',
    ]
    max_count = 1

    intro_text = RichTextField(blank=True)
    success_text = RichTextField(blank=True)

    content_panels = BannerPage.content_panels + [
        FieldPanel('intro_text', classname='full'),
        FieldPanel('success_text', classname='full'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['hide_newsletter_info'] = True
        return context

    def serve(self, request, *args, **kwargs):
        from subscription.forms import NewsletterSubscriptionForm
        context = self.get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = NewsletterSubscriptionForm(request.POST)
            if form.is_valid():
                subscriber = form.save(commit=False)
                if NewsletterSubscription.objects.filter(email=subscriber.email).exists():
                    context['error_message'] = """This email address is already subscribed. 
                    You will continue to receive updates."""
                else:
                    subscriber.save()
                return render(request, 'subscription/main_landing.html', context)
        else:
            form = NewsletterSubscriptionForm()

        context['form'] = form
        return render(request, 'subscription/main.html', context)


class NewsletterSubscription(models.Model):
    email = models.EmailField(
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
