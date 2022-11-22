from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGEHEIGHT = ((40, "400px"), (32, "320px"), (27, "270px"), (20, "220px"),
               (16, "160px"), (8, "88px"), (5, "50px"))
IMAGEPLACE = ((1, "Image-as-background"), (2, "Image-on-side"))
TEXTBACKGROUND = ((1, "No background"), (2, "Put background"))


class CarouselContent(models.Model):
    """Content model to generate content items, including
       customized header, size, number on one row, order & card template"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="content_posts"
    )
    
    featured_image = models.ImageField(null=True, blank=True, default='placeholder')
    featured_image_url = models.URLField(max_length=1024, null=True, blank=True)
    
    image_alt_text = models.CharField(max_length=200, blank=True,
                                      default='aden wellness theme image')
    header = models.CharField(max_length=200, blank=True)
    text_background = models.IntegerField(choices=TEXTBACKGROUND,
                                          default=1)
    excerpt = models.TextField(blank=True)
    image_height = models.IntegerField(choices=IMAGEHEIGHT, default=27)
    image_place = models.IntegerField(choices=IMAGEPLACE, default=1)
    image_order = models.IntegerField(default=1)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["image_order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home',)
