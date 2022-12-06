from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('more/<slug:slug>/', views.HomeContentDetail.as_view(), name='content_detail'),
    path('privacy/', views.view_privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name="contact_form"),
    path('message/', views.ContactView.as_view(), name='contact_form'),
]
