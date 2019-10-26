from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from core.models import BannerPage
from settings.models import Blog as BlogSettings
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


class BlogListingPage(BannerPage):
    """ Lists all blog pages. """

    template = 'blog/listing_page.html'
    max_count = 1
    subpage_types = [
        'blog.BlogDetailPage',
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        posts_per_page = BlogSettings.for_site(request.site).num_posts_per_page
        paginator = Paginator(all_posts, posts_per_page)
        page_nr = request.GET.get('page')
        try:
            posts = paginator.page(page_nr)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context


class BlogDetailPage(BannerPage):
    template = 'blog/post.html'
    subpage_types = []
    parent_page_type = [
        'blog.BlogListingPage',
    ]

    author = models.ForeignKey(
        BlogAuthor,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ('richtext', blocks.RichTextBlock()),
            ('image', blocks.FigureBlock()),
            ('code', blocks.CodeFragmentBlock()),
            ('HTML', RawHTMLBlock()),
            ('latex', blocks.MathBlock()),
            ('blockquote', BlockQuoteBlock()),
            ('embed', EmbedBlock()),
        ],
        blank=True,
    )

    content_panels = BannerPage.content_panels + [
        SnippetChooserPanel('author'),
        StreamFieldPanel('content'),
    ]
