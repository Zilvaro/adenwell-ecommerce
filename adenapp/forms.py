from django import forms
from django.contrib import messages
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Form for contact-message submission."""
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)