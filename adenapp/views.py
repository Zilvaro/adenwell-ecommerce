from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from .models import HomeContent, HomeMedia, ContactMessage
from .forms import ContactForm


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


def view_privacy_policy(request):
    """ A view that renders the bag contents page """

    return render(request, 'adenapp/privacy_policy.html')


def contact(request):
    """Renders the contact template."""
    if request.method == 'POST':
        first_name = request.POST['']
        last_name = models.CharField(max_length=80)
        email = models.EmailField()
        contact_message = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)

    return render(request, 'adenapp/contact_form.html', {})


class ContactView(SuccessMessageMixin, generic.CreateView):
    """The view to render the contact form for the registered user to leave
       a message to the admin."""
    model = ContactMessage
    template_name = 'adenapp/contact_form.html'
    fields = ('first_name', 'last_name', 'email', 'contact_message')
    success_message = "Thank You for your message!"
