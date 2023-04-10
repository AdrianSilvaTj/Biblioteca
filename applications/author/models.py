from django.db import models

# managers
from .managers import AuthorManager
# Create your models here.

class Author(models.Model):
    first_name = models.CharField('Nombres', max_length=50) 
    last_name = models.CharField('Apellidos', max_length=50)
    nationality = models.CharField('Nacionalidad', max_length=30)
    age = models.PositiveIntegerField()
    
    # Vinculamos el Manager con el Modelo Author
    objects = AuthorManager()
    
    def __str__(self):
        return self.first_name +' '+ self.last_name
