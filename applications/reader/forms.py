from django import forms

from applications.book.models import Book
from .models import Loan

class LoanForm(forms.ModelForm):
    
    class Meta:
        model = Loan
        fields = (
            'reader',
            'book'
        )
        
class LoanMultiAddForm(forms.ModelForm):
    
    # books, Creara un conjunto de valores basado en los registros del modelo 'Book' y se mostrará
    # como un conjunto de checkboxs
    books = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget = forms.CheckboxSelectMultiple,
    )
    
    class Meta:
        model = Loan
        fields = (
            'reader',
        )
            
    def __init__(self, *args, **kwargs):
        super(LoanMultiAddForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()
            
    