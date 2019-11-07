from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Movie(models.Model):

    title = models.CharField(
        max_length=128,
        blank=False,
    )
    director = models.CharField(
        max_length=128,
        blank=True,
    )
    genre = models.CharField(
        max_length=128,
        blank=True,
    )
    duration = models.DurationField(
        blank=True,
        null=True,
    )
    release_date = models.DateField(
        blank=False,
    )
    poster = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name='Poster',
    )
    trailer = models.URLField(
        blank=True,
    )

    panels = [
        FieldPanel('title', classname='title'),
        ImageChooserPanel('poster'),
        MultiFieldPanel(
            [
                FieldPanel('director'),
                FieldPanel('release_date'),
                FieldPanel('duration'),
                FieldPanel('genre'),
            ],
            heading='Details',
        ),
        MultiFieldPanel(
            [
                FieldPanel('trailer'),
            ],
            heading='External Links',
        ),
    ]

    @property
    def year(self):
        return self.release_date.year

    def __str__(self):
        return self.title

    def autocomplete_label(self):
        return str(self)
