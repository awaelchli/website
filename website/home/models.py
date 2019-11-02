from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

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
    ]

    class Meta:
        verbose_name = 'Home Page'


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
