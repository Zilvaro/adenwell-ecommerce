from django.contrib import admin
from .models import HomeContent, HomeMedia, ContactMessage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HomeContent)
class ContentAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'header', 'excerpt',)


@admin.register(HomeMedia)
class MediaAdmin(SummernoteModelAdmin):

    list_display = ('media_name', 'media_pid',)
    search_fields = ['media_name']
    summernote_fields = ('media_text',)


@admin.register(ContactMessage)
class ContactsAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'contact_message')
    search_fields = ['first_name', 'last_name', 'email']
