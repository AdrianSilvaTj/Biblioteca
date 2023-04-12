from django.db import models

# Create your models here.
class Persona(models.Model):
    '''Model definition for Persona.'''
    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('País', max_length=50)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)
    class Meta:
        '''Meta definition for Persona.'''

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        #db_table = 'persona' # define el nombre exacto de la tabla en base de datos
        unique_together = ['pais','apelativo'] # no permite que se repita la misma combinación de datos en esos campos
        
        # constraints, realiza validaciones
        # constraints = [
        #     models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        # ]
        abstract = True # Especifica que la clase es abstracta o Padre, y no se creara en la db

    def __str__(self):
        return self.full_name
    
class Empleado(Persona):
    empleo = models.CharField('Empleo', max_length=50)
    
class Cliente(Persona):
    email = models.CharField('Empleo', max_length=50)