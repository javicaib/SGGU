from django.forms import ValidationError
import re


def validar_patrones(valor, mensaje, patron=r'[0-9]'):
    p = re.compile(patron)
    if p.search(valor):
        raise ValidationError(mensaje)

    else:

        return valor


