from django.db import models

class Piloto(models.Model):
    nombre_completo = models.CharField(max_length=100)
    equipo = models.CharField(max_length=50)
    numero_carro = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_completo} - {self.equipo}"

class Sesion(models.Model):
    nombre_sesion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre_sesion} - {self.ubicacion}"

class DatosCarro(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    velocidad = models.FloatField()
    rpm = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Datos de {self.piloto.nombre_completo}"