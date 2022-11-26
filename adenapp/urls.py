from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("home/", views.HomeView.as_view(), name='home_view'),
]