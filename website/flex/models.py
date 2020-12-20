from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from core.models import BannerPage
from streams import blocks


class FlexPage(BannerPage):
    template = "flex/flex_page.html"
    subpage_types = [
        "flex.FlexPage",
    ]
    parent_page_type = [
        "home.HomePage",
        "flex.FlexPage",
    ]

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        blank=True,
    )

    content_panels = BannerPage.content_panels + [StreamFieldPanel("content")]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
