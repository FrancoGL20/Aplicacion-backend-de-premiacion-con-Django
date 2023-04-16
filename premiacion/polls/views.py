# Importa la función render para poder renderizar un template y la función get_object_or_404 para obtener un objeto de la base de datos o devolver un error 404 si no existe
from django.shortcuts import render, get_object_or_404
# Importa la función HttpResponse para poder devolver una respuesta HTTP
from django.http import HttpResponse
# Importa el modelo Question para poder usar sus atributos y métodos
from .models import Question

# Vista que se ejecuta cuando se llama a la ruta polls/
def index(request):
    """Vista que se ejecuta cuando se llama a la ruta polls/

    Args:
        request (HttpRequest): Objeto que contiene información sobre la petición HTTP

    Returns:
        render: Objeto que contiene la respuesta HTTP y el template a renderizar
    """
    # Obtiene todas las preguntas de la base de datos
    latest_question_list = Question.objects.all() 
    
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id): 
    """Vista que se ejecuta cuando se llama a la ruta polls/<question_id>/

    Args:
        request (HttpRequest): Objeto que contiene información sobre la petición HTTP
        question_id (int): Identificador de la pregunta

    Returns:
        render: Objeto que contiene la respuesta HTTP y el template a renderizar o un error 404 si no existe
    """
    # Obtiene la pregunta de la base de datos o devuelve un error 404 si no existe
    question=get_object_or_404(Question, pk=question_id)
    
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """Vista que se ejecuta cuando se llama a la ruta polls/<question_id>/results/

    Args:
        request (HttpRequest): Objeto que contiene información sobre la petición HTTP
        question_id (int): Identificador de la pregunta

    Returns:
        HttpResponse: Objeto que contiene la respuesta HTTP
    """
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}.")


def vote(request, question_id):
    """Vista que se ejecuta cuando se llama a la ruta polls/<question_id>/vote/

    Args:
        request (HttpRequest): Objeto que contiene información sobre la petición HTTP
        question_id (int): Identificador de la pregunta

    Returns:
        HttpResponse: Objeto que contiene la respuesta HTTP
    """
    return HttpResponse(f"Estás votando por la pregunta número {question_id}.")

