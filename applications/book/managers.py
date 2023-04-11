import datetime
from django.db import models
from django.db.models import Q,Count
from django.contrib.postgres.search import TrigramSimilarity

class BookManager(models.Manager):
    """Manager para el modelo Book"""
    def list_by_date(self,kword):
        result = self.filter(
            title__icontains=kword,
            date__range=('2000-01-01','2023-01-01')
            )        
        return result
    
    def list_by_date2(self,kword,d1,d2):
        """Listar libros por un rango de fecha dada en un formulario"""
        # strptime() cambia el formato de la fecha
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()
        
        result = self.filter(
            title__icontains=kword,
            date__range=(date1,date2)
            )        
        return result
 
    def list_by_category(self, category):
        """Listar libros por categoría y ordenarlos por titulo"""
        return self.filter(
            category__id=category
        ).order_by('title')
        
    def add_author(self, bk, author):
        """Agregar un autor a un libro que ya tiene registros, a traves de una relación Many to Many"""
        book = self.get(id=bk)
        # .add Agrega un autor a la tabla Many To Many a Book
        book.authors.add(author)
        return book
    
    def loan_count(self):
        """Contar la cantidad de prestamos de libros"""
        result = self.annotate(
            loan_num = Count('loan_related')
        )
        
        for bk in result:
            print('*********************')
            print(bk,'>>', bk.loan_num)
        return result
    
    def list_by_trigram(self,kword):
        """ Listar libros realizando la busqueda con la extension Trigram, la cual busca por
        similitudes a pesar de que las porciones de texto no sean exactas"""
        
        if kword:
            result = self.filter(
                title__trigram_similar=kword            
                )        
            return result
        else:
            return self.all()[:10]
        
class CategoryManager(models.Manager):
    """Manager para el modelo Category"""
    def list_by_authors(self,author):
        return self.filter(
            book_related__authors__id = author
        ).distinct()
        
    def list_book_count(self):
        """Contar la cantidad de libros por cada categoría"""
        # .annotate Agrega un campo virtual a la tabla
        # Count Cuenta los registros relacionados a traves de 'book_related'
        result = self.annotate(
            num_book=Count('book_related')
        )
        
        print('*********************')
        for bk in result:
            print(bk,'>>', bk.num_book)
        return result
    
