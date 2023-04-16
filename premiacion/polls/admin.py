from django.contrib import admin
from .models import Question, Choice

# Registrar el modelo Question para que aparezca en el sitio de administración
# NOTA: Para registra más de un modelo, se puede enviar una lista de modelos, pe:
# admin.site.register([Question, Choice])
admin.site.register(Question)
