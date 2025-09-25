from asyncio import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from Empresa.forms import TaskForm
from Empresa.models import Datos

def home(request):
    return render(request, "home.html")

@login_required
def datos_list(request):
    data = Datos.objects.all()
    return render(request, 'Datos.html', {'datos': data})

@login_required
def crear_datos (request):
    if request.method == 'GET':
        return render(request,
                   "crear_datos.html",
                   {"forms":TaskForm()})
    else:
        forms = TaskForm(request.POST)
        if forms.is_valid():
            new_task = forms.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('Datos')
        else:
           return render(request,
                      'crear_datos.html',
                      {'forms': forms,
                       'error': "por favor ingresa datos validos"})

def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, 
                  "signin.html",
                  {"form":AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          'signin.html',
                          {"form": AuthenticationForm(),
                           "error":"Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect("Datos")

def singup(request):
    if request.method == "GET":
        return render(request, 
                  "singup.html",
                  {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("Datos")

            except IntegrityError:
                return render(request,
                              'singup.html',
                              {"form": UserCreationForm(),
                               "error":"Error al crear el usuario"})

        else:
                 return render(request,
                              'singup.html',
                              {"form": UserCreationForm(),
                               "error":"Error, Las contraseñas no coinciden"})