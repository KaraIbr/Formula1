from django.contrib import admin
from .models import Piloto, Sesion

@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'equipo', 'numero_carro', 'pais', 'puntos', 'podios')
    search_fields = ('nombre_completo', 'equipo', 'pais')
    list_filter = ('equipo', 'pais')

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('nombre_sesion', 'ubicacion', 'tipo_sesion', 'fecha_inicio', 'clima', 'temperatura')
    search_fields = ('nombre_sesion', 'ubicacion', 'tipo_sesion')
    list_filter = ('tipo_sesion', 'ubicacion', 'clima')