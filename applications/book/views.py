from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Category
# Create your views here.


class BookByDateView(ListView):
    model = Book
    template_name = "book/list_by_date.html"
    context_object_name = "book_list"

    def get_queryset(self):
        kword = self.request.GET.get("kword",'') 
        # fecha 1
        d1 = self.request.GET.get("date1",'')       
        # fecha 2
        d2 = self.request.GET.get("date2",'')      
        
        if d1 and d2:
            return Book.objects.list_by_date2(kword,d1,d2)
        else:
            return Book.objects.list_by_date(kword)
        
class BookTrigramListView(ListView):
    model = Book
    template_name = "book/list_trigram.html"
    context_object_name = "book_list"
    
    def get_queryset(self):
        kword = self.request.GET.get("kword",'')
        return Book.objects.list_by_trigram(kword)
    
class BookByCategoryView(ListView):
    model = Book
    template_name = "book/list_by_category.html"
    context_object_name = "book_list" 
    
    def get_queryset(self):
        cat = 3
        return  Book.objects.list_by_category(cat)
    
class BookDetailView(DetailView):
    model = Book
    template_name = "book/details.html"
    
class CategoryOfAuthorView(ListView):
    model = Category
    template_name = "category/of_authors.html"
    context_object_name = "category_list"
    

