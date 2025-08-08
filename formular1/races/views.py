from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
import json
from django.shortcuts import render
from django.utils.decorator import method_decorator
from django.views.decorators.csrf    import csrf_exempt
from .models import Race

class ClientesView(View):
   @method_decorator(csrf_exempt, name='dispatch')
   //obtenemos datos con el metodo get ya solo es investigar como filtrar los datos
def get(self, request):
    races = Race.objects.all()
    data = [{'id': race.id, 'name': race.name} for race in races]
    return JsonResponse(data, safe=False)

def post(self, request):
    data = json.loads(request.body)
    race = Race.objects.create(name=data['name'])
    return JsonResponse({'message': 'Race created successfully'}, status=201)

def put(self, request, id):
    data = json.loads(request.body)
    race = Race.objects.get(id=id)
