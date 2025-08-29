from django.core.management.base import BaseCommand
from django.utils import timezone
from races.models import Piloto, Sesion, DatosCarro
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Carga datos iniciales de Fórmula 1 para pruebas'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos iniciales de Fórmula 1...')
        
        # Crear pilotos
        pilotos_data = [
            {'id_piloto': 'HAM', 'nombre_completo': 'Lewis Hamilton', 'equipo': 'Mercedes', 'pais': 'Reino Unido', 'numero_carro': 44},
            {'id_piloto': 'VER', 'nombre_completo': 'Max Verstappen', 'equipo': 'Red Bull', 'pais': 'Países Bajos', 'numero_carro': 1},
            {'id_piloto': 'LEC', 'nombre_completo': 'Charles Leclerc', 'equipo': 'Ferrari', 'pais': 'Mónaco', 'numero_carro': 16},
            {'id_piloto': 'NOR', 'nombre_completo': 'Lando Norris', 'equipo': 'McLaren', 'pais': 'Reino Unido', 'numero_carro': 4},
            {'id_piloto': 'ALO', 'nombre_completo': 'Fernando Alonso', 'equipo': 'Aston Martin', 'pais': 'España', 'numero_carro': 14},
            {'id_piloto': 'RUS', 'nombre_completo': 'George Russell', 'equipo': 'Mercedes', 'pais': 'Reino Unido', 'numero_carro': 63},
            {'id_piloto': 'SAI', 'nombre_completo': 'Carlos Sainz', 'equipo': 'Ferrari', 'pais': 'España', 'numero_carro': 55},
            {'id_piloto': 'PER', 'nombre_completo': 'Sergio Pérez', 'equipo': 'Red Bull', 'pais': 'México', 'numero_carro': 11},
        ]
        
        pilotos_creados = []
        for piloto_data in pilotos_data:
            piloto, created = Piloto.objects.get_or_create(
                id_piloto=piloto_data['id_piloto'],
                defaults=piloto_data
            )
            pilotos_creados.append(piloto)
            if created:
                self.stdout.write(f'Piloto creado: {piloto.nombre_completo}')
            else:
                self.stdout.write(f'Piloto ya existe: {piloto.nombre_completo}')
        
        # Crear sesiones
        sesiones_data = [
            {
                'id_sesion': 'GP_MONACO_2024',
                'nombre_sesion': 'Gran Premio de Mónaco 2024',
                'ubicacion': 'Circuito de Mónaco',
                'fecha_inicio': timezone.now() - timedelta(days=30),
                'fecha_fin': timezone.now() - timedelta(days=29)
            },
            {
                'id_sesion': 'GP_ESPANA_2024',
                'nombre_sesion': 'Gran Premio de España 2024',
                'ubicacion': 'Circuito de Barcelona-Cataluña',
                'fecha_inicio': timezone.now() - timedelta(days=15),
                'fecha_fin': timezone.now() - timedelta(days=14)
            },
            {
                'id_sesion': 'GP_CANADA_2024',
                'nombre_sesion': 'Gran Premio de Canadá 2024',
                'ubicacion': 'Circuito Gilles Villeneuve',
                'fecha_inicio': timezone.now() - timedelta(days=7),
                'fecha_fin': timezone.now() - timedelta(days=6)
            }
        ]
        
        sesiones_creadas = []
        for sesion_data in sesiones_data:
            sesion, created = Sesion.objects.get_or_create(
                id_sesion=sesion_data['id_sesion'],
                defaults=sesion_data
            )
            sesiones_creadas.append(sesion)
            if created:
                self.stdout.write(f'Sesión creada: {sesion.nombre_sesion}')
            else:
                self.stdout.write(f'Sesión ya existe: {sesion.nombre_sesion}')
        
        # Crear datos del carro
        self.stdout.write('Generando datos técnicos del carro...')
        datos_creados = 0
        
        for sesion in sesiones_creadas:
            for piloto in pilotos_creados:
                # Generar múltiples registros de datos por piloto y sesión
                for i in range(20):  # 20 registros por piloto por sesión
                    timestamp = sesion.fecha_inicio + timedelta(minutes=i*2)
                    
                    # Generar datos realistas
                    velocidad = random.randint(80, 350)  # km/h
                    rpm = random.randint(8000, 15000)
                    acelerador = random.uniform(0, 100)  # porcentaje
                    freno = random.choice([True, False])
                    
                    dato, created = DatosCarro.objects.get_or_create(
                        piloto=piloto,
                        sesion=sesion,
                        timestamp=timestamp,
                        defaults={
                            'velocidad': velocidad,
                            'rpm': rpm,
                            'acelerador': round(acelerador, 2),
                            'freno': freno
                        }
                    )
                    
                    if created:
                        datos_creados += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'¡Datos cargados exitosamente!\n'
                f'- {len(pilotos_creados)} pilotos\n'
                f'- {len(sesiones_creadas)} sesiones\n'
                f'- {datos_creados} registros de datos técnicos'
            )
        )
