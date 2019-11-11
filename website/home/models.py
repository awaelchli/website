import datetime

from django.db import models
from django.utils import timezone
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.models import Page, Orderable

from blog.models import BlogListingPage
from contact.models import ContactPage
from core.models import BannerPage
from flex.models import FlexPage
from streams import blocks


class HomePage(BannerPage):
    template = 'home/home_page.html'
    subpage_types = [
        'blog.BlogListingPage',
        'contact.ContactPage',
        'flex.FlexPage',
        'subscription.SubscriptionPage'
    ]
    parent_page_type = [
        'wagtailcore.Page',
    ]
    max_count = 1

    content = StreamField(
        [
            ('cards', blocks.CardBlock()),
        ],
        blank=True,
    )

    content_panels = BannerPage.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel('achievements', min_num=3, max_num=5),
            ],
            heading='Achievements'
        ),
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [
                InlinePanel('countdowns', max_num=1),
            ],
            heading='Countdown',
        ),
    ]

    class Meta:
        verbose_name = 'Home Page'

    @property
    def countdown(self):
        return self.countdowns.first()


class Countdown(Orderable):
    page = ParentalKey(
        'home.HomePage',
        related_name='countdowns',
    )
    title = models.CharField(
        max_length=100,
        blank=True,
    )

    target = models.DateTimeField(
        blank=False,
    )

    teaser_text = RichTextField(
        blank=True,
    )

    reveal_text = RichTextField(
        blank=True
    )

    reveal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('target'),
        FieldPanel('teaser_text'),
        FieldPanel('reveal_text'),
        PageChooserPanel('reveal_page'),
    ]

    @property
    def delta(self):
        # Clip negative time delta to 0
        return max(self.target - timezone.now(), datetime.timedelta(0))

    @property
    def seconds(self):
        return self.delta.seconds % 60

    @property
    def minutes(self):
        seconds = self.delta.seconds - self.seconds
        minutes = seconds // 60
        return minutes % 60

    @property
    def hours(self):
        seconds = self.delta.seconds - self.seconds
        hours = seconds // (60 * 60)
        return hours % 24

    @property
    def days(self):
        return self.delta.days

    @property
    def finished(self):
        return self.delta.seconds <= 0


class Statistics(Orderable):
    page = ParentalKey(
        'home.HomePage',
        related_name='achievements',
    )
    name = models.CharField(
        max_length=128,
        blank=False,
    )
    number = models.IntegerField(
        blank=False,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('number'),
    ]
