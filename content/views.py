from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from .models import CarouselContent


def view_brand_content(request):
    """ A view that renders the bag contents page """

    return render(request, 'content/content.html')


class ContentList(generic.TemplateView):
    """View to render the list of POSTs on the home page."""
    template_name = 'content.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['carousel_content'] = CarouselContent().objects.all()
        return context

