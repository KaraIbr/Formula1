import json
from django.core.management.base import BaseCommand
from races.models import Piloto, Sesion
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Carga datos iniciales desde archivo JSON'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        self.stdout.write('Limpiando datos existentes...')
        Sesion.objects.all().delete()
        Piloto.objects.all().delete()

        # Cargar archivo JSON
        with open('races/data/f1_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Cargar Pilotos
        self.stdout.write('Cargando pilotos...')
        for piloto_data in data['pilotos']:
            Piloto.objects.create(
                nombre_completo=piloto_data['nombre_completo'],
                equipo=piloto_data['equipo'],
                numero_carro=piloto_data['numero_carro'],
                pais=piloto_data['pais'],
                puntos=piloto_data['puntos'],
                podios=piloto_data['podios'],
                victorias=piloto_data['victorias'],
                poles=piloto_data['poles'],
                vueltas_rapidas=piloto_data['vueltas_rapidas'],
                edad=piloto_data['edad']
            )

        # Cargar Sesiones
        self.stdout.write('Cargando sesiones...')
        for sesion_data in data['sesiones']:
            Sesion.objects.create(
                nombre_sesion=sesion_data['nombre_sesion'],
                ubicacion=sesion_data['ubicacion'],
                fecha_inicio=parse_datetime(sesion_data['fecha_inicio']),
                fecha_fin=parse_datetime(sesion_data['fecha_fin']),
                tipo_sesion=sesion_data['tipo_sesion'],
                clima=sesion_data['clima'],
                temperatura=sesion_data['temperatura'],
                humedad=sesion_data['humedad'],
                velocidad_viento=sesion_data['velocidad_viento'],
                direccion_viento=sesion_data['direccion_viento'],
                probabilidad_lluvia=sesion_data['probabilidad_lluvia'],
                longitud_circuito=sesion_data['longitud_circuito'],
                numero_vueltas=sesion_data['numero_vueltas']
            )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))