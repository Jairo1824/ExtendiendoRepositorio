from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar , Predica

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
    

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"
        exclude=["user"]

class PredicaFormulario (forms.ModelForm):
    class Meta:
        model = Predica
        fields = "__all__"

