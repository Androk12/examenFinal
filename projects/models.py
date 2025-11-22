from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class project(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=400)
    stock = models.PositiveIntegerField(default=0)
    anio = models.PositiveIntegerField(default=2000)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(default=timezone.now)


def clean(self):
        if self.stock < 0:
            raise ValidationError("El stock no puede ser negativo.")
        if self.anio_publicacion < 0:
            raise ValidationError("El año de publicación no puede ser negativo.")
    