from django import forms
from App.Estudiante.models import Estudiante


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
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),

        }
        extra_kwargs = {"password": {'write_only': True}}