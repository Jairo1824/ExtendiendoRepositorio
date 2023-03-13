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


def sumate(request):

    if request.method == "POST":
        mi_formulario = persona_formulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            persona = Persona (nombre = informacion["nombre"] ,
                                apellido = informacion["apellido"],
                                fecha_nacimiento=informacion["fecha_nacimiento"],
                                email=informacion["email"],
                                )
            persona.save()



            return redirect('inicio')
        else:

            return render(request, "AppGeneral/inicio.html", {"mensaje":"Lamentamos que,Algo no salio bien con tu solicitud. Intentalo nuevamente o mas tarde"})
        
    
    else:
        mi_formulario= persona_formulario()
    
        return render ( request, "sumate.html",{"formulario_miembro":mi_formulario})
    
