from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from streams import blocks


@register_snippet
class BlogAuthor(models.Model):

    first_name = models.CharField(
        max_length=128,
    )
    last_name = models.CharField(
        max_length=128,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name'),
                FieldPanel('last_name'),
            ],
            heading='Details'
        )
    ]

    class Meta:
        verbose_name = 'Blog Author'
        verbose_name_plural = 'Blog Authors'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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

    author = models.ForeignKey(
        BlogAuthor,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
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
        SnippetChooserPanel('author'),
        StreamFieldPanel('content'),
    ]
