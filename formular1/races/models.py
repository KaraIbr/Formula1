from django.db import models

class Piloto(models.Model):
    nombre_completo = models.CharField(max_length=100)
    equipo = models.CharField(max_length=50)
    numero_carro = models.IntegerField()
    pais = models.CharField(max_length=50, default='No especificado')
    puntos = models.IntegerField(default=0)
    podios = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    poles = models.IntegerField(default=0)
    vueltas_rapidas = models.IntegerField(default=0)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_completo} - {self.equipo}"

    class Meta:
        ordering = ['-puntos']

class Sesion(models.Model):
    nombre_sesion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tipo_sesion = models.CharField(max_length=50, default='Práctica')
    clima = models.CharField(max_length=50, default='Despejado')
    temperatura = models.IntegerField(default=25)
    humedad = models.IntegerField(default=0)
    velocidad_viento = models.IntegerField(default=0)
    direccion_viento = models.CharField(max_length=10, default='N')
    probabilidad_lluvia = models.IntegerField(default=0)
    longitud_circuito = models.FloatField(default=0.0)
    numero_vueltas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_sesion} - {self.ubicacion}"

    class Meta:
        ordering = ['fecha_inicio']