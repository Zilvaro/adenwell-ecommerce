from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.ContentDetail.as_view(),
         name='content_detail'),
]