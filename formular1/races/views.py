from django.shortcuts import render
from django.http import JsonResponse
from .models import Piloto, Sesion, DatosCarro

def index(request):
    """Vista principal que muestra todos los datos"""
    data = {
        'pilotos': list(Piloto.objects.values()),
        'sesiones': list(Sesion.objects.values()),
        'datos_carro': list(DatosCarro.objects.values())
    }
    return JsonResponse(data)

def lista_pilotos(request):
    """API endpoint para listar pilotos"""
    pilotos = list(Piloto.objects.values())
    return JsonResponse({'pilotos': pilotos})