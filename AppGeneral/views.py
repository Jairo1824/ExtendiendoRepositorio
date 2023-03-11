from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from AppGeneral.forms import *
from AppGeneral.models import *
from django.shortcuts import redirect
# Create your views here.

def saludo (request):
   nombre="Jairo"
   plantilla=loader.get_template("saludo.html")
   contexto={"nombre":nombre}
   documento=plantilla.render(contexto)

   return HttpResponse(documento)




def crear_persona (request):

    if request.method =="post":
        mi_formulario=PersonaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            persona=Persona(nombre=informacion["nombre"],
                            apellido=informacion["apellido"],
                            fecha_nacimiento=informacion["fecha_nacimiento"],
                            email=informacion["email"])
        persona.save()
        return redirect ("saludo")    
        

    return render (request,"AppGeneral/Templates/index.html")