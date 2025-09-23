from django.forms import ModelForm
from .models import Datos


class TaskForm(ModelForm):
    class Meta:
        model = Datos
        fields = ['title', 'descripcion','importante']