from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable

from blog.models import BlogListingPage
from contact.models import ContactPage
from flex.models import FlexPage


class HomePage(Page):
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

    banner_title = models.CharField(
        max_length=128,
        blank=False,
    )
    banner_subtitle = models.CharField(
        max_length=128,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
            ],
            heading='Achievements'
        ),
        MultiFieldPanel(
            [
                InlinePanel('achievements', min_num=3, max_num=5),
            ],
            heading='Achievements'
        )
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
