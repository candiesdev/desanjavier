from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usuario", views.usuario, name="usuario"),
    path("formulario", views.formulario, name="formulario"),
    path("registro_confirmacion", views.registro_confirmacion, name="registro_confirmacion"),
]