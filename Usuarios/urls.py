"""Usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App.Controllers.IndexController import IndexController
from App.Controllers.CursosController import CursosController
from App.Controllers.UserController import UserController
urlpatterns = [
    #Obtenemos los parametro que se ingresan a traves de la url para ejcutar las vista segun el parametro
    path('', IndexController.index, name='index'),
    path('about', IndexController.about, name='about'),
    path('admin/', admin.site.urls, name='login'),
    path('cursos', CursosController.index, name='cursos'),
    path('details/<int:cursoid>/',CursosController.details, name='details'),
    path('obtener', CursosController.obtener_curso, name='obtener'),
    path('register', UserController.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
