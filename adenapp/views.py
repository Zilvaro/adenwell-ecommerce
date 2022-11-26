from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from .models import HomeContent, HomeMedia


class HomeView(generic.TemplateView):
    """View to render the content, category links on the home page."""

    template_name = 'adenapp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['content'] = HomeContent.objects.all()
        context['homepage_media'] = HomeMedia.objects.all()
        return context
