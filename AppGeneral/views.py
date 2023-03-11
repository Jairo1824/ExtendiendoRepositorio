from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from AppGeneral.forms import *
from AppGeneral.models import *
from django.shortcuts import redirect
# Create your views here.


def saludo(request):
    

    return render(request,"AppGeneral/saludo.html")


def miembros (request): 

    return render  (request,"AppGeneral/crear-persona.html")