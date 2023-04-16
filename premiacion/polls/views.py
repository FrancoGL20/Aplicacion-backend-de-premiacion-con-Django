# Módulo que contiene las vistas de la aplicación polls
from django.shortcuts import render
# Importa la función HttpResponse para poder devolver una respuesta HTTP
from django.http import HttpResponse


# Vista que se ejecuta cuando se llama a la ruta polls/
def index(request): # request es un objeto que contiene información sobre la petición HTTP
    return HttpResponse("Estás en la página principal de la aplicación polls.")


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}.")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Estás votando por la pregunta número {question_id}.")

