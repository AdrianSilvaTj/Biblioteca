from django.db import models

from applications.author.models import Person
from applications.book.models import Book
from .managers import LoanManager

class Reader(Person):
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    class Meta:        
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
    
class Loan(models.Model):
    '''Model definition for Loan.'''
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Lector')
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        verbose_name='Titulo del Libro',
        related_name='loan_related'
    )
    date = models.DateField('Fecha de Préstamo')
    devolution_date = models.DateField('Fecha de Devolución',blank=True,null=True)
    returned = models.BooleanField('Devuelto',default=False)
    
    objects = LoanManager()
    
    class Meta:
        '''Meta definition for Loan.'''
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return self.book.title +'-->'+self.reader.first_name

    def save(self, *args, **kwargs):
        """ Resta al estock del libro al momento de guardar el prestamo """
        print ('Entro en save--------------')
        self.book.stock = self.book.stock -1
        self.book.save()        
        return super(Loan, self).save(*args, **kwargs)