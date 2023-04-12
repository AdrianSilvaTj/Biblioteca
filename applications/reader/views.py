from datetime import date
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Loan
from .forms import LoanForm

class LoanRegister(FormView):
    template_name = 'reader/loan_add.html'
    form_class = LoanForm
    success_url = '.'
    
    def form_valid(self, form):
        """ Verifica y asigna los valores y luego guarda el nuevo registro.
        Varias maneras de hacerlo """
        
        # Metodo 1
        # Loan.objects.create(
        #     reader=form.cleaned_data['reader'],
        #     book=form.cleaned_data['book'],
        #     date = date.today(),
        #     returned = False
        # )
        
        # Metodo 2
        loan = Loan(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            date = date.today(),
            returned = False            
        )
        loan.save()
        
        # Restar del stock del libro
        # book = form.cleaned_data['book']
        # book.stock = book.stock - 1
        # book.save()
                
        return super(LoanRegister,self).form_valid(form)