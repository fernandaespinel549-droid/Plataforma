from django.contrib import admin
from .models import Datos

@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ('title', 'descripcion', 'importante')
