from django.contrib import admin
from .models import CarouselContent
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CarouselContent)
class CarouselContentAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'header', 'excerpt',)
