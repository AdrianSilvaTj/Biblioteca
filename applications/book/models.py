from django.db import models

from applications.author.models import Author
from .managers import BookManager,CategoryManager

# Create your models here.
class Category(models.Model):
    '''Model definition for Category.'''
    name = models.CharField('Nombre', max_length=30)
    objects = CategoryManager()
    
    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class Book(models.Model):
    '''Model definition for Book.'''
    title = models.CharField('Titulo', max_length=100)
    # 'related_name' sirve para acceder desde category a un book
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='book_related'    
    )
    authors = models.ManyToManyField(Author)
    date = models.DateField('Fecha de Lanzamiento')
    image = models.ImageField(upload_to='book',blank=True,null=True)
    visits = models.PositiveIntegerField('Visitas')
    
    objects = BookManager()

    class Meta:
        '''Meta definition for Book.'''
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title', 'date']

    def __str__(self):
        return str(self.id) + ' - ' + self.title