from datetime import date
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .models import Loan
from .forms import LoanForm, LoanMultiAddForm

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
    
class LoanAdd(FormView):
    template_name = 'reader/loan_add.html'
    form_class = LoanForm
    success_url = '.'
    
    def form_valid(self, form):
        """ get_or_create, Verifica si ya un objeto se ha creado segun las condiciones que se le pasa
        por parámetro, sino existe se crea con esos datos y con los que se le pase por 'defaults='
        'obj', En caso de crearse, guarda el objeto (queryset). 'created' boolean, indica si existe o no """
        obj, created = Loan.objects.get_or_create(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            returned = False,
            defaults = {'date' : date.today()}            
        )
        
        if created:                               
            return super(LoanAdd,self).form_valid(form)
        else:            
            return HttpResponseRedirect('/')
    
class LoanMultiAdd(FormView):
    template_name = 'reader/loan_multi_add.html'
    form_class = LoanMultiAddForm
    success_url = '.'
    
    def form_valid(self, form):
        """ Registrar los multiples libros prestados. Se crea una lista con todos los
        registros para luego guardarlos. Es mas optimo que realizar varios procesos de guardado"""        
        loan_arr = []
        for ln in form.cleaned_data['books']:
            loan = Loan(
                reader=form.cleaned_data['reader'],
                book=ln,
                date = date.today(),
                returned = False
            )
            loan_arr.append(loan)
        # bulk_create, Registrar en lotes   
        Loan.objects.bulk_create(loan_arr)
        
        return super(LoanMultiAdd,self).form_valid(form)
        