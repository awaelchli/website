from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class BlogListingPage(Page):
    """ Lists all blog pages. """

    template = 'blog/listing_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogDetailPage.objects.live().public()
        return context


class BlogDetailPage(Page):
    template = 'blog/post.html'

    subtitle = models.CharField(
        max_length=128,
        blank=True,
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ('full_richtext', blocks.RichTextBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('image'),
        StreamFieldPanel('content'),
    ]
