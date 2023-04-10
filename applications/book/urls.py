from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view(), name='list_all'),
]