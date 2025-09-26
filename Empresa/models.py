from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Datos(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    creacion = models.DateField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo_empleado = models.CharField(max_length=100, null=True, blank=True)
    cedula = models.CharField(max_length=10, default="")
    fecha_ingreso = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    

    def __str__(self):
        return f"{self.nombre} - {self.user}"