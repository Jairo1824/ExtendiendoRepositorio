from django.contrib import admin
from django.urls import path
from AppGeneral import views
from django.contrib.auth.views import LogoutView

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
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("register/",views.register,name="register"),
    path("editar-perfil/",views.editar_perfil, name="editar-perfil"),
    path("manejo-usuarios/",views.manejo_usuarios, name="manejo-usuarios"),
    path("agregar-avatar/",views.agregar_avatar, name="agregar-avatar"),
    path("predicas/",views.predicas, name="predicas"),
    path("agregar-predica/",views.agregar_predica, name="agregar-predica"),




]