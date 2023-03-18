from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template,Context
from AppGeneral.forms import *
from AppGeneral.models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def manejo_usuarios(request):
    return render(request,"manejo-usuarios.html")



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


@login_required
def leer_personas(request):
    personas=Persona.objects.all()

    contexto={"personas":personas}

    return render(request,"leer-personas.html",contexto)


@login_required
def eliminar_personas(request,persona_email):
    persona=Persona.objects.get(email=persona_email)
    persona.delete()

    personas= Persona.objects.all()

    contexto={"personas":personas}

    return render(request,"leer-personas.html",contexto)


@login_required
def editar_personas(request, persona_email):

    # Recibe el nombre del profesor que vamos a modificar
    persona = Persona.objects.get(email=persona_email)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = persona_formulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            persona.nombre = informacion['nombre']
            persona.apellido = informacion['apellido']
            persona.fecha_nacimiento = informacion['fecha_nacimiento']
            persona.email = informacion['email']

            persona.save()

            # Vuelvo al inicio o a donde quieran
            return redirect('leer-personas')
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = persona_formulario(initial={'nombre': persona.nombre, 'apellido': persona.apellido,
                                                   'fecha_nacimiento': persona.fecha_nacimiento,'email': persona.email })

    # Voy al html que me permite editar
    return render(request, "editar-personas.html", {"miFormulario": miFormulario, "persona_email": persona.email})



def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return redirect("/")
            else:
                return render(request, "login.html", {"mensaje":"Datos incorrectos"})
        
        else:

            return render(request, "login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html",{"form":form})

@login_required
def register(request):

    if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

    return render(request,"register.html" ,  {"form":form})



@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return redirect("/")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editar-perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

