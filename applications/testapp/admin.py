from django.contrib import admin

from applications.testapp.models import Empleado, Cliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)