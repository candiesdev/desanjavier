from django import forms
from django.forms import ModelForm

# FORMULARIO PARA EL INGRESO DE USUARIO PARA LOGIN O CREAR

class FormUsername(forms.Form):
    username = forms.CharField(label="Usuario", max_length=25, required=True)
    user_action = forms.CharField(widget=forms.HiddenInput)