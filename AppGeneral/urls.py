from django.contrib import admin
from django.urls import path
from AppGeneral import views

urlpatterns = [
    path('saludo/', views.saludo, name= "saludo"),
    path("",views.inicio,name="inicio"),
    path("equipo/",views.equipo,name="equipo"),
    path("padre/",views.padre,name="padre"),
    path("sumate/",views.sumate,name="sumate"),
    path("leer-personas/",views.leer_personas,name="leer-personas"),
    path("eliminar-personas/<persona_email>",views.eliminar_personas,name="eliminar-personas"),
    path("editar-personas/<persona_email>",views.editar_personas,name="editar-personas"),
    path("login/",views.login_request,name="login"),




]