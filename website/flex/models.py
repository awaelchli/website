from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from streams import blocks


class FlexPage(Page):
    template = 'flex/flex_page.html'

    subtitle = models.CharField(
        max_length=128,
        blank=True
    )

    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('rich_text', blocks.RichTextBlock()),
            ('simple_rich_text', blocks.SimpleRichTextBlock()),
            ('cards', blocks.CardBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Flexible Page'
        verbose_name_plural = 'Flexible Pages'
