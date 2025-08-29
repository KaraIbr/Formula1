from django.shortcuts import render
from django.http import JsonResponse
from .models import Piloto, Sesion

def index(request):
    """Vista principal"""
    context = {
        'pilotos': Piloto.objects.all(),
        'sesiones': Sesion.objects.all(),
    }
    return render(request, 'races/index.html', context)

def lista_pilotos(request):
    """API endpoint para listar pilotos"""
    pilotos = list(Piloto.objects.all().values())
    return JsonResponse({'pilotos': pilotos})