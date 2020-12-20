from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


@register_snippet
class Menu(ClusterableModel):

    title = models.CharField(
        max_length=128,
    )
    slug = AutoSlugField(
        populate_from='title',
        editable=True,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('slug'),
            ],
            heading='Menu'
        ),
        InlinePanel('menu_items', label='Menu Item')
    ]

    def __str__(self):
        return self.title


class MenuItem(Orderable):

    link_title = models.CharField(
        max_length=128,
        blank=True,
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    open_in_new_tab = models.BooleanField(
        blank=True,
        default=False,
    )
    page = ParentalKey(
        Menu,
        related_name='menu_items',
    )

    panels = [
        FieldPanel('link_title'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return '#'

    @property
    def title(self):
        if self.link_title:
            return self.link_title
        elif self.link_page:
            return self.link_page.title
        else:
            return 'Missing Title'
