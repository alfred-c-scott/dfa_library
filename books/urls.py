# /books/urls.py
from xmlrpc.client import Boolean
from django.urls import path

from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home')
]