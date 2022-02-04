from django.contrib import admin
from .models import Cursos,Categorias
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")
    search_fields = ('Nombre',)
    list_filter = ('Nombre', 'Estado')
    
admin.site.register(Categorias,CategoriasAdmin)

class CursosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cursos,CursosAdmin)    