from django.db import models
from django.contrib.auth.models import User

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

class Avatar(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.user}-{self.imagen}"