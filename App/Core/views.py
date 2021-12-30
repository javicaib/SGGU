from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App.Seguridad.decorador import group_required
from django.db import connection

# Create your views here.
@login_required
def inicio(request):
    return render(request,'index.html')
@login_required
@group_required('Admin')
def listar_Estudiantes(request):
    return render(request,'listar.html')