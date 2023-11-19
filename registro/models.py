from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# MODELO PARA REGISTRO DE DATOS DE USUARIOS.

class DatosAsociado(models.Model):
    user_id = models.IntegerField()
    user_creacion = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=250)
    documento = models.CharField(max_length=20)
    documento_emision_selector = [
        ("be", "BE"),
        ("ch", "CH"),
        ("co", "CO"),
        ("lp", "LP"),
        ("or", "OR"),
        ("pa", "PA"),
        ("po", "PO"),
        ("sc", "SC"),
        ("ta", "TA"),
        ("na", "Otro"),
    ]
    documento_emision = models.CharField(max_length=2, choices=documento_emision_selector, default="sc")
    nacimiento_lugar = models.CharField(max_length=150)
    nacimiento_fecha = models.DateField()
    telefono = models.CharField(max_length = 20)
    correo = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=250)
    ocupacion = models.CharField(max_length=250)
    notificaciones = models.BooleanField(default=True)