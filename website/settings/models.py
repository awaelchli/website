from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting


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
