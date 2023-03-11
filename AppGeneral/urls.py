from django.contrib import admin
from django.urls import path
from AppGeneral import views

urlpatterns = [
    path('', views.saludo),
    path('sumate/', views.crear_persona, name= "sumate"),


]