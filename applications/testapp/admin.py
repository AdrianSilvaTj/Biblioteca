from django.contrib import admin

from applications.testapp.models import Empleado, Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Empleado)