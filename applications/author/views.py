from django.shortcuts import render
from django.views.generic import ListView

from .models import Author
# Create your views here.


class AuthorListView(ListView):
    model = Author
    template_name = "author/list_all.html"

    def get_queryset(self):
        kword = self.request.GET.get("kword",'')        
        # return Author.objects.searchFullName(kword)
        # return Author.objects.searchExcludeAge(kword)
        return Author.objects.searchLtGt(kword)
    