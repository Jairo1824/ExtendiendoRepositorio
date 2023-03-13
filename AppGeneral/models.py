from django.db import models

# Create your models here.
class Persona (models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    email=models.EmailField()

    def __str__(self) -> str:
        nombre=self.nombre
        apellido=self.apellido

        texto= nombre+" "+apellido

        return texto
    
class Noticia (models.Model):
    email=models.EmailField()