from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    templates = 'home/home_page.html'
    max_count = 1
    banner_title = models.CharField(
        max_length=128,
        default=''
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title')
    ]

    class Meta:
        verbose_name = 'Home Page'
