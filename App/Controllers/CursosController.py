from django.shortcuts import render
from App.Models.Cursos_models import Cursos_models
class CursosController():
    def index(request):
        cursos_list =  Cursos_models.cursos_list()
        context = {'cursos_list': cursos_list}
        return render(request, 'views/cursos/cursos.html',context)

    def details(request,cursoid):
        objects =  Cursos_models.getcurso(cursoid)
        context = {'curso': objects[0],'categoria': objects[1]}
        return render(request, 'views/cursos/details.html',context)