from django.db import models
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from core.models import BannerPage
from subscription.utils import generate_subscriber_uuid


class SubscriptionPage(RoutablePageMixin, BannerPage):
    template = 'subscription/subscribe.html'
    subpage_types = []
    parent_page_type = [
        'home.HomePage',
    ]
    max_count = 1

    email_intro_text = RichTextField(
        blank=True,
        verbose_name='Intro Text',
    )
    email_success_text = RichTextField(
        blank=True,
        verbose_name='Success Text',
    )
    telegram_intro_text = RichTextField(
        blank=True,
        verbose_name='Intro Text',
    )

    content_panels = BannerPage.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('email_intro_text'),
                FieldPanel('email_success_text'),
            ],
            heading='Email'
        ),
        MultiFieldPanel(
            [
                FieldPanel('telegram_intro_text')
            ],
            heading='Telegram'
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['hide_newsletter_info'] = True
        return context

    @route(r'^$')
    @route(r'^subscribe/$', name='subscribe')
    def subscribe(self, request, *args, **kwargs):
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
                return render(request, 'subscription/subscribe_landing.html', context)
        else:
            form = NewsletterSubscriptionForm()

        context['form'] = form
        return render(request, 'subscription/subscribe.html', context)

    @route(r'^unsubscribe/([0-9a-f]{32})/$', name='unsubscribe')
    def unsubscribe(self, request, uuid, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        subscription = NewsletterSubscription.objects.filter(uuid=uuid).first()
        if subscription:
            subscription.delete()
            context['email'] = subscription.email
        return render(request, 'subscription/cancellation.html', context)

    def get_unsubscribe_url_for(self, subscription):
        return self.get_full_url() + self.reverse_subpage('unsubscribe', args=(subscription.uuid, ))


class NewsletterSubscription(models.Model):
    email = models.EmailField(
        blank=False
    )
    uuid = models.CharField(
        max_length=32,
        blank=True,
        default=generate_subscriber_uuid
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email
