from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class persona_formulario (forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()


class NoticiaFormulario (forms.Form):
    email=forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
    