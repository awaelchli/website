# Generated by Django 2.2.6 on 2019-11-03 19:58

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations

import streams.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_auto_20191103_2017"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetailpage",
            name="content",
            field=wagtail.core.fields.StreamField(
                [
                    ("richtext", streams.blocks.RichTextBlock()),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "code",
                        wagtail.core.blocks.StreamBlock(
                            [
                                (
                                    "code",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "language",
                                                wagtail.core.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("bash", "Bash + Shell"),
                                                        ("batch", "Batch"),
                                                        ("c", "C"),
                                                        ("cpp", "C++"),
                                                        ("css", "CSS"),
                                                        ("django", "Django/Jinja2"),
                                                        ("git", "Git"),
                                                        ("java", "Java"),
                                                        ("javascript", "JavaScript"),
                                                        ("json", "JSON"),
                                                        ("latex", "LaTeX"),
                                                        ("makefile", "Makefile"),
                                                        ("markdown", "Markdown"),
                                                        ("matlab", "MATLAB"),
                                                        ("python", "Python"),
                                                        ("regex", "Regex"),
                                                        ("sql", "SQL"),
                                                        ("yaml", "YAML"),
                                                    ],
                                                    help_text="Coding language",
                                                    identifier="language",
                                                    label="Language",
                                                ),
                                            ),
                                            (
                                                "code",
                                                wagtail.core.blocks.TextBlock(
                                                    identifier="code", label="Code"
                                                ),
                                            ),
                                        ],
                                        label="Code",
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("HTML", wagtail.core.blocks.RawHTMLBlock(icon="fa-html5")),
                    (
                        "latex",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "equation",
                                    wagtail.core.blocks.TextBlock(required=True),
                                ),
                                (
                                    "size",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            (100, "100%"),
                                            (150, "150%"),
                                            (200, "200%"),
                                            (250, "250%"),
                                        ]
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("blockquote", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "youtube",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "video_id",
                                    wagtail.core.blocks.RegexBlock(
                                        label="Video ID",
                                        max_length=11,
                                        min_length=11,
                                        regex="^[a-zA-Z0-9_-]{11}$",
                                        required=True,
                                    ),
                                ),
                                (
                                    "aspect_ratio",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("1by1", "1:1"),
                                            ("4by3", "4:3"),
                                            ("16by9", "16:9"),
                                            ("21by9", "21:9"),
                                        ],
                                        label="Aspect Ratio",
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
