from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('loan/add/', views.LoanAdd.as_view(), name='loan_add'),
    path('loan/multi_add/', views.LoanMultiAdd.as_view(), name='loan_multi_add'),
]