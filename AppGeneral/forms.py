from django import forms

# Create your models here.
class persona_formulario (forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()


class NoticiaFormulario (forms.Form):
    email=forms.EmailField()