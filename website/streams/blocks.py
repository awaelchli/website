from django.core.validators import RegexValidator
from wagtail.core import blocks
from wagtail.core.blocks import StreamBlock
from wagtail.images.blocks import ImageChooserBlock
import wagtailcodeblock.blocks


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

    title = blocks.CharBlock(
        required=True,
    )
    subtitle = blocks.CharBlock(
        required=False,
    )

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True)),
                ('text', blocks.TextBlock(required=True)),
                ('page', blocks.PageChooserBlock(required=False)),
                ('url', blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'streams/card_block.html'
        icon = 'fa-th-large'
        label = 'Cards'


class CodeFragmentBlock(StreamBlock):

    code = wagtailcodeblock.blocks.CodeBlock(
        label='Code'
    )

    caption = blocks.TextBlock(
        required=False
    )

    class Meta:
        icon = 'code'
        label = 'Code Fragment'


class FigureBlock(blocks.StructBlock):

    image = ImageChooserBlock(
        required=True
    )
    caption = blocks.TextBlock(
        required=False,
    )

    class Meta:
        template = 'streams/figure_block.html'
        icon = 'image'
        label = 'Image'


class MathBlock(blocks.StructBlock):

    equation = blocks.TextBlock(
        required=True
    )

    size = blocks.ChoiceBlock(
        choices=[
            (100, '100%'),
            (150, '150%'),
            (200, '200%'),
            (250, '250%'),
        ],
        default=150,
        required=True
    )

    caption = blocks.TextBlock(
        required=False
    )

    class Meta:
        template = 'streams/math_block.html'
        icon = 'code'
        label = 'LaTeX'

    def clean(self, value):
        eq = value['equation']
        eq = eq.strip().strip('$')
        eq = eq.replace('\\[', '').replace('\\]', '')
        eq = eq.replace('\\(', '').replace('\\)', '')
        eq = eq.strip()
        value['equation'] = eq
        return value


class YouTubeBlock(blocks.StructBlock):

    video_id = blocks.RegexBlock(
        regex=r'^[a-zA-Z0-9_-]{11}$',
        max_length=11,
        min_length=11,
        required=True,
        label='Video ID',
    )

    aspect_ratio = blocks.ChoiceBlock(
        choices=[
            ('1by1', '1:1'),
            ('4by3', '4:3'),
            ('16by9', '16:9'),
            ('21by9', '21:9'),
        ],
        default='16by9',
        required=True,
        label='Aspect Ratio',
    )

    class Meta:
        template = 'streams/youtube_block.html'
        icon = 'fa-youtube-play'
        label = 'YouTube Video'

