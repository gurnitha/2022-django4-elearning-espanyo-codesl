from django.shortcuts import render
class CursosController():
    def index(request):
        return render(request, 'views/cursos/cursos.html')