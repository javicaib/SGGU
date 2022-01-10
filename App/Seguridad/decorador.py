from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from App.Estudiante.models import Estudiante


def group_required(*group_names):
    def check(user):
        if user.groups.filter(name__in=group_names).exists() | user.is_superuser:
            return True
        else:
            raise PermissionDenied(HttpResponseForbidden)

    return user_passes_test(check)


def password_required(*val):
    def check(estudiante):
        if estudiante.cambiar_pass:
            return True
        else:
            raise PermissionDenied(HttpResponseForbidden)

    return user_passes_test(check)
