from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from AppMensajes.forms import *
from AppMensajes.models import *
from django.shortcuts import redirect

def mensaje(request):
    mi_formulario= MensajeFormulario(request.POST)

    if request.method=="POST":
        mi_formulario = MensajeFormulario(request.POST)

        if mi_formulario.is_valid():
            mi_formulario.save()
            return redirect("/")
        
    else:
        return render(request,"mensaje.html",{"mi_formulario":mi_formulario})