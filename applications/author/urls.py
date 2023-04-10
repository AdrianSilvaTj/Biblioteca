from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name='list_all'),
]