from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_brand_content, name='view_brand_content'),
]