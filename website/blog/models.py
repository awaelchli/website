from abc import abstractmethod

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.blocks import RawHTMLBlock, StreamBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core.signals import page_published
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailautocomplete.edit_handlers import AutocompletePanel

from core.models import BannerPage
from settings.models import Blog as BlogSettings
from streams import blocks
from subscription.notification import notify_subscribers


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
    parent_page_type = [
        'home.HomePage',
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        all_posts = self.get_children().live().public().order_by('-first_published_at')
        all_posts = [p.specific for p in all_posts]
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
            ('HTML', RawHTMLBlock(icon='fa-html5')),
            ('latex', blocks.MathBlock()),
            ('blockquote', blocks.BlockQuoteBlock()),
            ('youtube', blocks.YouTubeBlock()),
        ],
        blank=True,
    )

    content_panels = BannerPage.content_panels + [
        SnippetChooserPanel('author'),
        StreamFieldPanel('content'),
    ]


class CreationBase(BlogDetailPage):
    subpage_types = []
    parent_page_type = []

    @property
    @abstractmethod
    def creation(self):
        pass


class VideoProjectPage(CreationBase):
    template = 'blog/creative_hub/post.html'
    subpage_types = []
    parent_page_type = [
        'blog.CreativeHub',
    ]

    video = StreamField(
        StreamBlock(
            [
                ('youtube', blocks.YouTubeBlock())
            ],
            min_num=1,
            max_num=1
        )
    )

    content_panels = CreationBase.content_panels + [
        StreamFieldPanel('video'),
    ]

    def creation(self):
        return self.video


class CreativeHub(BlogListingPage):
    """ Lists all creative project pages. """
    class Meta:
        verbose_name = 'Creative Hub'

    template = 'blog/creative_hub/listing_page.html'
    max_count = 1
    subpage_types = [
        'blog.VideoProjectPage',
    ]
    parent_page_type = [
        'home.HomePage',
    ]


class MovieReview(BlogDetailPage):
    template = 'blog/post.html'
    subpage_types = []
    parent_page_type = [
        'blog.BlogListingPage',
    ]

    movie = models.ForeignKey(
        'movies.Movie',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel('author'),
        AutocompletePanel('movie'),
        StreamFieldPanel('content'),
    ]


# Send notifications for certain types of posts
page_published.connect(notify_subscribers, sender=BlogDetailPage)
page_published.connect(notify_subscribers, sender=VideoProjectPage)
page_published.connect(notify_subscribers, sender=MovieReview)
