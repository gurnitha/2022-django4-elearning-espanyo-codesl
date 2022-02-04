from django.db import models
from ..models import Cursos,Categorias
class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('Nombre')
        return cursos
    def getcurso(idcurso):
        curso = Cursos.objects.filter(CursoId=idcurso) 
        for item in curso:
            categoria = Categorias.objects.get(CategoriaID=item.CategoriaID.CategoriaID)
        return [item,categoria]   