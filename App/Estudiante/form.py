from django import forms
from App.Estudiante.models import Estudiante
from App.Core.validacion import validar_patrones


class FormularioEstudianteEdit(forms.ModelForm):
    username = forms.CharField(max_length=20,
                               min_length=3,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=20,
                                 min_length=3,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))



    def clean_username(self):
        user = self.cleaned_data['username']
        mensaje = 'El nombre de usuario solo puede tener letras'
        return validar_patrones(user, mensaje)

    def clean_first_name(self):
        nombre = self.cleaned_data['first_name']

        mensaje = 'El nombre solo puede tener letras'

        return validar_patrones(nombre, mensaje)

    def clean_last_name(self):
        apellido = self.cleaned_data['last_name']
        mensaje = 'El apellido solo puede tener letras'
        return validar_patrones(apellido, mensaje)

    class Meta:
        model = Estudiante
        fields = ['username',
                  'last_name',
                  'first_name',
                  'facultad',
                  'grupo',

                  ]
        widgets = {

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),

        }


class FormularioEstudianteCambiarPass(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    class Meta:
        model = Estudiante
        fields = [
            'password'

        ]
        widgets = {

            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }


class FormularioEstudianteCreate(forms.ModelForm):
    first_name = forms.CharField(max_length=20,
                                 min_length=3,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_first_name(self):
        nombre = self.cleaned_data['first_name']

        mensaje = 'El nombre solo puede tener letras'

        return validar_patrones(nombre, mensaje)

    def clean_last_name(self):
        apellido = self.cleaned_data['last_name']
        mensaje = 'El apellido solo puede tener letras'
        return validar_patrones(apellido, mensaje)

    class Meta:
        model = Estudiante
        fields = [
            'last_name',
            'first_name',
            'facultad',
            'grupo',

        ]
        widgets = {

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),

        }
