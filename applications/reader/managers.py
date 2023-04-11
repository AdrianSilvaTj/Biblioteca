from django.db import models

from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower

class LoanManager(models.Manager):
    """ Manager para Prestamo """
    
    def readers_book_average(self,book):
        """ Mostrar promedio y suma de edades de lectores de un libro """
        result = self.filter (
            book__id = book
        ).aggregate(
            age_avg = Avg('reader__age'),
            age_sum = Sum('reader__age')
        )
        return str(result['age_avg']) +'->'+ str(result['age_sum'])
    
    def book_loan_count(self):
        """ Lista los libros prestados y la cantidad de prestamos de cada uno"""
        # .values Se utiliza para indicarle a 'annotate' que cuente y agrupe por el campo indicado, no
        # por el 'id' como lo hace por defecto, al utilizar 'values' el resultado es un diccionario
        
        result = self.values(
            'book'
        ).annotate(
            loan_count = Count('book'),
            title = Lower('book__title')
        )
        
        for lo in result:
            print('*****************')
            print(lo,lo['loan_count'])
        return result