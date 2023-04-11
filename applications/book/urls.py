from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('book_by_date/', views.BookByDateView.as_view(), name='list_by_date'),
    path('book_by_category/', views.BookByCategoryView.as_view(), name='list_by_category'),
    path('book/<pk>', views.BookDetailView.as_view(), name='detail'),
    path('book_trigram/', views.BookTrigramListView.as_view(), name='list_trigram'),
]