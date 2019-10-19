from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class FlexPage(Page):
    template = 'flex/flex_page.html'

    subtitle = models.CharField(
        max_length=128,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]

    class Meta:
        verbose_name = 'Flexible Page'
        verbose_name_plural = 'Flexible Pages'
