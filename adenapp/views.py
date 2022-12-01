from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from .models import HomeContent, HomeMedia, SiteDocs


class HomeView(generic.TemplateView):
    """View to render the content, category links on the home page."""

    template_name = 'adenapp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['content'] = HomeContent.objects.all()
        context['homepage_media'] = HomeMedia.objects.all()
        return context


class HomeContentDetail(generic.DetailView):
    """View to render the details of selected Content."""
    def get(self, request, slug, *args, **kwargs):
        queryset = HomeContent.objects.filter(status=1)

        content = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "adenapp/content_detail.html",
            {
               "content": content,
            },
        )


class DocsView(generic.DetailView):
    """View to render the document content upon request."""

    def get(self, request, doc_id, *args, **kwargs):
        queryset = SiteDocs().objects.filter(status=1)

        document = get_object_or_404(queryset, doc_id=doc_id)

        return render(
            request,
            "adenapp/document_detail.html",
            {
               "document": document,
            },
        )
