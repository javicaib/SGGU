from django.contrib.auth.models import User


def generar_correo_estudiante(valor):
    email = valor + '@estudiantes.uci.cu'
    return email


def generar_usuario(nombre, apellidos):
    nombre = nombre.split()
    apellidos = apellidos.split()

    usuario = nombre[0][0] + apellidos[0]

    if User.objects.filter(username=usuario).exists():
        nombre_param = nombre[0]
        apellidos_param = apellidos[1]
        return generar_usuario(nombre_param, apellidos_param)

    else:
        return usuario
