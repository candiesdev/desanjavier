from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FormUsername
from registro.models import DatosAsociado
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, DateInput, modelformset_factory, BaseFormSet

# INDEX PARA LA APLICACIÓN DE REGISTRO DE USUARIOS

def index(request, mensaje_index=""):
  return render(request, "registro/index.html", {"mensaje_index": mensaje_index})

# FORMULARIO QUE SOLICITA Y VALIDA USUARIO PARA LOGIN O CREAR

def usuario(request):
    user_alert = "Ingresar"
    alert_color = "text-success"
    user_action = "login"
    if "prev" in request.GET:
        prev = request.GET["prev"]
    else:
        prev = "/"
    if "action" in request.GET:
        if request.GET["action"] == "nuevo":
            user_alert = "Registrar un nuevo usuario"
            alert_color = "text-success"
            user_action = "create"
    else:
        user_action = "login"
    if request.method == "POST":
        form = FormUsername(request.POST)
        if form.is_valid():
            if request.POST['user_action'] == "login":
                user_alert = "Inicio de sesión no disponible"
                alert_color = "text-danger"
                return render(request, "registro/login_confirmacion.html", {
                    "user_alert": user_alert,
                    "alert_color": alert_color})
            elif request.POST['user_action'] == "create":
                user_exist = DatosAsociado.objects.filter(user_name__iexact=request.POST['username'])
                if user_exist:
                    user_action = "create"
                    user_alert = "Usuario no disponible"
                    alert_color = "text-danger"
                else:
                    return redirect(f"/registro/formulario?usuario={request.POST['username']}")
                return render(request, "registro/user.html", {
                    "form": form,
                    "user_alert": user_alert,
                    "alert_color": alert_color
                })

    else:
        form = FormUsername(initial={"user_action": user_action})

    return render(request, "registro/user.html", {
        "form": form,
        "user_alert": user_alert,
        "alert_color": alert_color
    })

# FUNCIÓN QUE ARMA EL FORMSET PARA DATOS DEL USUARIO

def formulario_populate(user_name=""):
    DatosFormSet_Populate = modelformset_factory(DatosAsociado, extra=1,
    fields=[
        "user_id",
        "user_name",
        "nombre",
        "apellido",
        "documento",
        "documento_emision",
        "nacimiento_lugar",
        "nacimiento_fecha",
        "telefono",
        "correo",
        "direccion",
        "ocupacion",
        "notificaciones",
    ],
    labels = {
        "user_id": _("Código"),
        "user_name": _("Usuario"),
        "nombre": _("Nombre"),
        "apellido": _("Apellido"),
        "documento_emision": _("Lugar de emisión"),
        "nacimiento_lugar": _("Lugar de nacimiento"),
        "nacimiento_fecha": _("Fecha de nacimiento"),
        "telefono": _("Teléfono"),
        "correo": _("Correo"),
        "ocupacion": _("Ocupación"),
        "notificaciones": _("Acepto recibir notifiaciones referente a las actividades de la asociación a través de chat, correo electrónico o llamadas telefónicas"),
    },
    error_messages = {
        "user_id": {
            "required": _("Este campo es requerido.")
        },
        "user_name": {
            "required": _("Este campo es requerido.")
        },
        "nombre": {
            "required": _("Este campo es requerido.")
        },
        "apellido": {
            "required": _("Este campo es requerido.")
        },
        "documento_emision": {
            "required": _("Este campo es requerido.")
        },
        "nacimiento_lugar": {
            "required": _("Este campo es requerido.")
        },
        "nacimiento_fecha": {
            "required": _("Este campo es requerido.")
        },
        "telefono": {
            "required": _("Este campo es requerido.")
        },
        "correo": {
            "required": _("Este campo es requerido.")
        },
        "ocupacion": {
            "required": _("Este campo es requerido.")
        },
    },
    widgets = {
        "user_id": TextInput(attrs={
            "value" : 0,
             "type" : "hidden"}),
        "user_name": TextInput(attrs={
            "placeholder" : "Hasta 15 caracteres sin espacio",
            "value": user_name,
            "readonly": True}),
        "nacimiento_fecha": DateInput(attrs={
            "type": "date"}),
    }
    )
    return(DatosFormSet_Populate)

# FORMULARIO DE DATOS DEL USUARIO

def formulario(request):
    if "usuario" in request.GET:
        user_name = request.GET["usuario"]
    else:
        user_name = ""
    alerta = ""
    alerta_color = ""
    DatosFormSet = formulario_populate(user_name)
    if request.method == "POST":
        formset = DatosFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # formset.save()
            return redirect("/registro/registro_confirmacion")
        else:
            alerta_color = "red"
            alerta = "Error en el formulario"
    else:
        formset = DatosFormSet(queryset=DatosAsociado.objects.none())
    return render(request, "registro/formulario.html", {"formset": formset, "alerta": alerta, "alerta_color": alerta_color})

# CONFIRMACIÓN DE REGISTRO DE NUEVO USUARIO

def registro_confirmacion(request):
    return render(request, "registro/registro_confirmacion.html")