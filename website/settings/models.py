from django.core.validators import RegexValidator
from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting
class GoogleAnalytics(BaseSetting):

    name = models.CharField(
        max_length=128,
        blank=True,
    )
    tracking_id = models.CharField(
        max_length=14,
        blank=True,
        verbose_name='Tracking ID',
        validators=[
            RegexValidator(
                regex=r'^[uU][aA]-\d{4,9}-\d{1,4}$',  # UA-XXXXXXXXX-X
                message='Enter a valid Google Analytics Tracking ID.',
            )
        ]
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('tracking_id'),
            ],
            heading='Details'
        )
    ]

    class Meta:
        verbose_name = 'Google Analytics'


@register_setting
class SocialMedia(BaseSetting):

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    github = models.URLField(blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('twitter'),
                FieldPanel('youtube'),
                FieldPanel('github'),
            ],
            heading='Social Media Settings'
        )
    ]

    class Meta:
        verbose_name = 'Social Media'


@register_setting
class Blog(BaseSetting):

    num_posts_per_page = models.PositiveIntegerField(
        verbose_name='Posts per page',
        help_text='The number of blog posts that appear in one page. ',
        default=5,
    )

    panels = [
        FieldPanel('num_posts_per_page')
    ]

    class Meta:
        verbose_name = 'Blog'
