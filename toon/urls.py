# toon/urls.py
from django.urls import path

from toon.views import upload


urlpatterns = [
    path('', upload, name='upload'),
]
