from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from .blocks import StoryBlock

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    @property
    def get_posts(self):
        return (
            self.get_children().live().order_by('-first_published_at')
        )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPostPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)

    body = StreamField(StoryBlock(), use_json_field=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPostGalleryImage(Orderable):
    page = ParentalKey(BlogPostPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name="+")
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]

