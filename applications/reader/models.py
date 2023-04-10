from django.db import models

from applications.book.models import Book

# Create your models here.
class Reader(models.Model):
    first_name = models.CharField('Nombres', max_length=50) 
    last_name = models.CharField('Apellidos', max_length=50)
    nationality = models.CharField('Nacionalidad', max_length=30)
    edad = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.first_name +' '+ self.last_name
    
class Loan(models.Model):
    '''Model definition for Loan.'''
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Lector')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Titulo del Libro')
    date = models.DateField('Fecha de Préstamo')
    devolution_date = models.DateField('Fecha de Devolución',blank=True,null=True)
    returned = models.BooleanField('Devuelto',default=False)
    
    class Meta:
        '''Meta definition for Loan.'''
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return self.book.title +'-->'+self.reader.first_name

