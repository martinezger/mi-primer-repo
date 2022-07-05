from unittest.util import _MAX_LENGTH
from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField() # camada == número == comisión de curso

    def __str__(self):
        return f"{self.nombre} {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()