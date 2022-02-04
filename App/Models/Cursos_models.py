from django.db import models
from ..models import Cursos,
class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('Nombre')
        return cursos