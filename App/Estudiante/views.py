from django.shortcuts import render, get_object_or_404
from App.Estudiante.form import FormularioEstudiante
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App.Seguridad.decorador import group_required
from App.Estudiante.models import Estudiante
from App.Core.funciones import capitalizar
from django.core.paginator import Paginator


# Create your views here.
@login_required
@group_required('Admin')
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
            email = usuario + '@estudiantes.uci.cu'
            facultad = request.POST.get('facultad')
            contra = request.POST.get('password2')

            estudiante = Estudiante(first_name=capitalizar(nombre), last_name=capitalizar(apellidos), grupo=grupo,
                                    username=usuario, email=email,
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
    # PAGINACION
    paginator = Paginator(estudiantes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'estudiantes': estudiantes,
        'page_obj': page_obj,

    }
    return render(request, 'listar.html', context)


@login_required
@group_required('Admin')
def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return HttpResponseRedirect('/listar_estudiantes')


@login_required
@group_required('Admin')
def editar_estudiante(request,update_id):

    estudiante = get_object_or_404(Estudiante, id=update_id)

    if request.method != 'POST':
        form = FormularioEstudiante(instance=estudiante)


    else:
        form = FormularioEstudiante(instance=estudiante, data=request.POST)
        if form.is_valid():
            estudiante.first_name = capitalizar(form.data.get('first_name'))
            estudiante.last_name = capitalizar(form.data.get('last_name'))
            estudiante.username = form.data.get('username')
            estudiante.grupo = form.data.get('grupo')
            estudiante.email = form.data.get('username') + '@estudiantes.uci.cu'
            estudiante.facultad = form.data.get('facultad')
            contra = form.data.get('password2')
            estudiante.set_password(contra)

            estudiante.save()
            return HttpResponseRedirect('/listar_estudiantes')

    context = {'form': form, 'estudiante': estudiante}
    return render(request, 'c_estudiante.html', context)