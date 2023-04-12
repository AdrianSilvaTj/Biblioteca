from django.db import models
# managers
from .managers import AuthorManager

class Person(models.Model):
    first_name = models.CharField('Nombres', max_length=50) 
    last_name = models.CharField('Apellidos', max_length=50)
    nationality = models.CharField('Nacionalidad', max_length=30)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id)+' - ' +self.first_name +' '+ self.last_name

    class Meta:
        abstract = True
    
class Author(Person):  
     
    alias = models.CharField("Pseudónimo", max_length=50, blank=True, default='alias')
    # Vinculamos el Manager con el Modelo Author
    objects = AuthorManager()
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

