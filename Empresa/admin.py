from django.contrib import admin
from .models import Datos

@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','cargo_empleado','cedula', 'fecha_ingreso', 'salario', 'creacion', 'importante', 'user')
