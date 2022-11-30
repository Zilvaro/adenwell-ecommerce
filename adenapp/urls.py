from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('more/<slug:slug>/', views.HomeContentDetail.as_view(), name='content_detail'),
]
