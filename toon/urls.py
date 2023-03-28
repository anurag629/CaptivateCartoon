# toon/urls.py
from django.urls import path

from toon.views import index


urlpatterns = [
    path('', index),
]
