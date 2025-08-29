import json
from django.core.management.base import BaseCommand
from races.models import Piloto, Sesion, DatosCarro
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Carga datos iniciales desde archivo JSON'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        self.stdout.write('Limpiando datos existentes...')
        DatosCarro.objects.all().delete()
        Sesion.objects.all().delete()
        Piloto.objects.all().delete()

        # Cargar archivo JSON
        with open('races/data/f1_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cargar Pilotos
        pilotos_map = {}
        for piloto_data in data['pilotos']:
            piloto = Piloto.objects.create(
                nombre_completo=piloto_data['nombre_completo'],
                equipo=piloto_data['equipo'],
                numero_carro=piloto_data['numero_carro']
            )
            pilotos_map[piloto.id] = piloto

        # Cargar Sesiones
        sesiones_map = {}
        for sesion_data in data['sesiones']:
            sesion = Sesion.objects.create(
                nombre_sesion=sesion_data['nombre_sesion'],
                ubicacion=sesion_data['ubicacion'],
                fecha_inicio=parse_datetime(sesion_data['fecha_inicio']),
                fecha_fin=parse_datetime(sesion_data['fecha_fin'])
            )
            sesiones_map[sesion.id] = sesion

        # Cargar Datos de Carro
        for datos_data in data['datos_carro']:
            DatosCarro.objects.create(
                piloto=pilotos_map[datos_data['piloto_id']],
                sesion=sesiones_map[datos_data['sesion_id']],
                velocidad=datos_data['velocidad'],
                rpm=datos_data['rpm'],
                timestamp=parse_datetime(datos_data['timestamp'])
            )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))