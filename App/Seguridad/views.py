from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.template import RequestContext
from  App.Seguridad.form import FormularioEstudiante


# Create your views here.
def login(request):
    return render(request, 'login.html')


def salir(request):
    logout(request)
    return redirect('/')


def forbbiden(request):
    return render(request, '403.html')

