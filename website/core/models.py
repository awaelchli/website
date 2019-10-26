from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class BannerPage(Page):
    banner_title = models.CharField(
        max_length=128,
        blank=True,
    )
    banner_subtitle = models.CharField(
        max_length=128,
        blank=True,
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                ImageChooserPanel('banner_image'),
            ],
            heading='Banner'
        )
    ]
