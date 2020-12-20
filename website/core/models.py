from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class BannerPage(Page):
    banner_title = models.CharField(
        max_length=128,
        blank=True,
        verbose_name="Title",
    )
    banner_subtitle = models.CharField(
        max_length=128,
        blank=True,
        verbose_name="Subtitle",
    )

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name="Image",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner",
        )
    ]
