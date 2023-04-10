from django.shortcuts import render
from django.views.generic import ListView

from .models import Book
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "book/list_all.html"

    def get_queryset(self):
        kword = self.request.GET.get("kword",'')        
        return Book.objects.searchLtGt(kword)
    