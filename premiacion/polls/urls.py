# Módulo que contiene las rutas de la aplicación polls
from django.urls import path

# Importa el módulo views.py de la aplicación polls para poder usar sus funciones
from . import views

# Lista de rutas de la aplicación polls
urlpatterns = [    
    # ex: /polls/ (donde polls es el nombre de la aplicación)
    path("", views.index, name="index"), # La ruta "" es la ruta raíz de la aplicación
    
    # ex: /polls/5/ (donde 5 es el valor de question_id)
    path("<int:question_id>/", views.detail, name="detail"),
    
    # ex: /polls/5/results/ (donde 5 es el valor de question_id)
    path("<int:question_id>/results/", views.results, name="results"),
    
    # ex: /polls/5/vote/ (donde 5 es el valor de question_id)
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
