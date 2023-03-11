from django import forms

# Create your models here.
class PersonaFormulario (forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    fecha_nacimiento=forms.DateField()
    email=forms.EmailField()

    def __str__(self) -> str:
        nombre=self.nombre
        apellido=self.apellido

        texto= nombre+" "+apellido

        return texto