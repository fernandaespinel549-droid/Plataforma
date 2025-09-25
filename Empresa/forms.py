from django.forms import ModelForm
from .models import Datos


class TaskForm(ModelForm):
    class Meta:
        model = Datos
        fields = ['nombre', 'apellido','cargo_empleado', 'cedula','fecha_ingreso','salario', 'importante']