from django.contrib import admin
from django.utils.html import format_html
from .models import Cursos,Categorias
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")
    search_fields = ('Nombre',)
    list_filter = ('Nombre', 'Estado')
    
admin.site.register(Categorias,CategoriasAdmin)

class CursosAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img width="85" height="45" src="/media/{}" />'.format(obj.Imagen))
    readonly_fields = ['image_tag']
    pass

admin.site.register(Cursos,CursosAdmin)    