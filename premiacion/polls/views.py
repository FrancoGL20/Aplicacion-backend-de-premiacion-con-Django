# Módulo que contiene las vistas de la aplicación polls
from django.shortcuts import render
# Importa la función HttpResponse para poder devolver una respuesta HTTP
from django.http import HttpResponse

# Vista que se ejecuta cuando se llama a la ruta polls/
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")