from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(
        required=True,
    )
    text = blocks.TextBlock(
        required=True
    )

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Full RichText'


class SimpleRichTextBlock(blocks.RichTextBlock):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple RichText'


class CardBlock(blocks.StructBlock):
    """Cards with one image, text and some button(s)"""

    title = blocks.CharBlock(
        required=True,
    )
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True)),
                ('text', blocks.TextBlock(required=True)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'streams/card_block.html'
        icon = 'edit'
        label = 'Cards'
