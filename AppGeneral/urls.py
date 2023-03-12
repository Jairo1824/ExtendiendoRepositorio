from django.contrib import admin
from django.urls import path
from AppGeneral import views

urlpatterns = [
    path('saludo/', views.saludo, name= "saludo"),
    path("",views.inicio,name="inicio"),
    path("equipo/",views.equipo,name="equipo"),
    path("padre/",views.padre,name="padre"),
    path("sumate/",views.sumate,name="sumate"),




]