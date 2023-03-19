from django.db import models

class Mensaje (models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField()
    Mensaje=models.TextField()