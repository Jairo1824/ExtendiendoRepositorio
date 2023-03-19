from django.contrib import admin
from django.urls import path
from AppMensajes import views

urlpatterns = [
    path('mensaje/', views.mensaje, name= "mensaje"),



]
