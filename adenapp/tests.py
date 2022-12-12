from django.test import TestCase, Client
from django.urls import reverse
from adenapp.models import HomeContent, ContactMessage


class TestViews (TestCase):

    def setup(self):
        self.client = Client()
        self.content_detail.url = reverse('content_detail', args=['content1'])
        HomeContent.objects.create(
            title='content1',
        )
        self.content_detail.url = reverse('home')
        self.content_detail.url = reverse('contact_form')


    def test_adenapp_home_content_detail_GET(self):
        response = self.client.get(reverse(content_detail.url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, adenapp/content_detail.html)


    def test_adenapp_home_view_GET(self):
        response = self.client.get(reverse(home.url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, adenapp/index.html)


    def test_contact_GET(self):
        response = self.client.get(reverse(contact_form.url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, adenapp/contact_form.html)
