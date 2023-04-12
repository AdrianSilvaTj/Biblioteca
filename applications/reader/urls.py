from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('loan/add/', views.LoanRegister.as_view(), name='loan_add'),
]