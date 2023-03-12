from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from AppGeneral.forms import *
from AppGeneral.models import *
from django.shortcuts import redirect
# Create your views here.




def saludo (request): 
    nombre="Pepe"
    contexto={"nombre":nombre}
    return render  (request,"saludo.html",contexto)

def inicio (request): 

    return render  (request,"inicio.html")

def equipo (request): 

    return render  (request,"equipo.html")

def padre (request): 

    return render  (request,"padre.html")


def sumate (request): 

    return render  (request,"sumate.html")