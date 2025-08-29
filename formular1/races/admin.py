from django.contrib import admin
from .models import Piloto, Sesion, DatosCarro

@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'equipo', 'numero_carro')

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('nombre_sesion', 'ubicacion', 'fecha_inicio', 'fecha_fin')

@admin.register(DatosCarro)
class DatosCarroAdmin(admin.ModelAdmin):
    list_display = ('piloto', 'sesion', 'velocidad', 'rpm', 'timestamp')