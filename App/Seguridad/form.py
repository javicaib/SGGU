from django import forms
from App.Seguridad.models import Estudiante


class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['username',
                  'last_name',
                  'email',
                  'first_name',
                  'facultad',
                  'grupo',
                  'password'
                  ]
