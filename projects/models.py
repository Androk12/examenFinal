from django.db import models

class project(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=400)
    