from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGEPLACE = ((1, "Image-as-background"), (2, "Image-on-side"))
TEXTBACKGROUND = ((1, "No background"), (2, "Put background"))
CAROUSEL = ((1, "First block"), (2, "Second block"), (3, "Third block"))


class HomeContent(models.Model):
    """Content model to generate content items, including
       customized header, size, number on one row, order & card template"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content_image_url = models.URLField(max_length=1024, null=True, blank=True)
    content_image = models.ImageField(null=True, blank=True)
    image_alt_text = models.CharField(max_length=200, blank=True,
                                      default='aden wellness theme image')
    header = models.CharField(max_length=200, blank=True)
    text_background = models.IntegerField(choices=TEXTBACKGROUND,
                                          default=1)
    excerpt = models.TextField(blank=True)
    carousel_block = models.IntegerField(choices=CAROUSEL, default=1)
    image_place = models.IntegerField(choices=IMAGEPLACE, default=1)
    image_order = models.IntegerField(default=1)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["image_order"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home',)


class HomeMedia(models.Model):
    """A model to generate and keep images and texts for use in click-menu
       visuals on the home page"""
    media_name = models.CharField(max_length=200, unique=True)
    media_id = models.IntegerField(default=0)
    media_image_url = models.URLField(max_length=1024, null=True, blank=True)
    media_image = models.ImageField(null=True, blank=True)
    media_image_alt_text = models.CharField(max_length=200,
                                            blank=True, default='aden image')
    media_text = models.TextField(blank=True)

    def __str__(self):
        return self.media_name
