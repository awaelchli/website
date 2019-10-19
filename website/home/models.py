from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    template = 'home/home_page.html'
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
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
    ]

    class Meta:
        verbose_name = 'Home Page'
