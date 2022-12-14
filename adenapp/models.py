from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGEPLACE = ((1, "Image-as-background"), (2, "Image-on-side"))
IMAGEORDER = ((1, "First/only"), (2, "Second"), (3, "Third"))
CAROUSEL = ((1, "First block"), (2, "Second block"), (3, "Third block"))


class HomeContent(models.Model):
    """Content model to generate content items, including
       customized header, size, number on one row, order & card template"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    header = models.CharField(max_length=200, blank=True)
    excerpt = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default='See more')
    content_image_url = models.URLField(max_length=1024, null=True, blank=True)
    content_image = models.ImageField(null=True, blank=True)
    image_alt_text = models.CharField(max_length=200, blank=True,
                                      default='aden wellness theme image')
    carousel_block = models.IntegerField(choices=CAROUSEL, default=1)
    image_order = models.IntegerField(choices=IMAGEORDER, default=1)
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
    media_pid = models.IntegerField(default=0)
    media_image_url = models.URLField(max_length=1024, null=True, blank=True)
    media_image = models.ImageField(null=True, blank=True)
    media_image_alt_text = models.CharField(max_length=200,
                                            blank=True, default='aden image')
    media_text = models.TextField(blank=True)

    def __str__(self):
        return self.media_name


class ContactMessage(models.Model):
    """Model to record the Content message"""
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    contact_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home',)
