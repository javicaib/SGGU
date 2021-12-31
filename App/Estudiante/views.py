from django.shortcuts import render
from App.Estudiante.form import FormularioEstudiante
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App.Seguridad.decorador import group_required
from App.Estudiante.models import Estudiante


# Create your views here.
def add_etudiante(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormularioEstudiante(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            usuario = request.POST.get('username')
            apellidos = request.POST.get('last_name')
            grupo = request.POST.get('grupo')
            nombre = request.POST.get('first_name')
            email = request.POST.get('email')
            facultad = request.POST.get('facultad')
            contra = request.POST.get('password')
            
            estudiante = Estudiante(first_name=nombre, last_name=apellidos, grupo=grupo, username=usuario, email=email,
                                    facultad=facultad)
            estudiante.set_password(contra)
            estudiante.save()

            form = FormularioEstudiante()
            # redirect to a new URL:
            return HttpResponseRedirect('listar_estudiantes')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormularioEstudiante()

    return render(request, 'c_estudiante.html', {'form': form})


@login_required
@group_required('Admin')
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    context = {
        'estudiantes': estudiantes
    }
    return render(request, 'listar.html', context)
