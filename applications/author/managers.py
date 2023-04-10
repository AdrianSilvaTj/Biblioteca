from django.db import models
from django.db.models import Q

class AuthorManager(models.Manager):
    """Manager para el modelo Author"""
    def search(self,kword):
        result = self.filter(first_name__icontains=kword)        
        return result
    
    def searchFullName(self,kword):
        # 'Q' para hacer consultas 'o' 'or'
        result = self.filter(
            Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
            )        
        return result
    
    def searchExcludeAge(self,kword):
        # 'exclude' excluir por una condición 
        result = self.filter(
            Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
            ).exclude(
                Q(age=28) | Q(age=48)
            )
            # tambien se podrian agregar '.filter'        
        return result
    
    def searchLtGt(self,kword):
        # '__gt' '__lt' mayor que, menor que
        result = self.filter(
            age__gt=40,
            age__lt=65
        ).order_by('last_name', 'first_name')        
        return result