# Módulo que contiene las rutas de la aplicación polls
from django.urls import path

# Importa el módulo views.py de la aplicación polls para poder usar sus funciones
from . import views

# Lista de rutas de la aplicación polls
urlspatterns = [
    # Ruta que llama a la función index del módulo views.py
    path("", view.index, name="index")
]
