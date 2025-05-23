from django.db import models

class RegistroSensor(models.Model):
    humedad = models.FloatField()
    riego_activado = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Humedad: {self.humedad}% - Riego: {'Sí' if self.riego_activado else 'No'}"
