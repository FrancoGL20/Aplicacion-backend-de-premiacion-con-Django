from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    # El id no es necesario, Django lo crea por defecto
    
    # El campo CharField es un campo de texto 
    question_text=models.CharField(max_length=200) # El primer argumento es la longitud máxima del texto
    
    # El campo DateTimeField es un campo de fecha y hora con el formato de fecha y hora predeterminado  (YYYY-MM-DD HH:MM:SS)
    pub_date=models.DateTimeField('date published') # El primer argumento es el nombre que se mostrará en el sitio de administración
    
    # El método __str__ es el método que se ejecuta cuando se imprime el objeto
    def __str__(self):
        # Retorna el texto de la pregunta
        return self.question_text
    
    def was_published_recently(self):
        # Retorna True si la pregunta fue publicada recientemente, False en caso contrario
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    # El id no es necesario, Django lo crea por defecto
    
    # El campo ForeignKey es una relación con otro modelo
    question=models.ForeignKey(Question, on_delete=models.CASCADE) # El primer argumento es el modelo al que se hace referencia, el segundo argumento es el comportamiento al eliminar el registro al que se hace referencia
    
    # El campo CharField es un campo de texto
    choice_text=models.CharField(max_length=200) # El primer argumento es la longitud máxima del texto
    
    # El campo IntegerField es un campo de número entero
    votes=models.IntegerField(default=0) # El primer argumento es el valor por defecto
    
    # El método __str__ es el método que se ejecuta cuando se imprime el objeto
    def __str__(self):
        # Retorna el texto de la opción
        return self.choice_text