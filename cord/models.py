from django.db import models

class GPS(models.Model):
    longitud = models.FloatField()
    latitud = models.FloatField()

    def __str__(self):
        return f"Longitud: {self.longitud}, Latitud: {self.latitud}"
