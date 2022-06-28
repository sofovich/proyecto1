
import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import EmailField

# Create your models here.
class Estudiante(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   email = models,EmailField()

class profes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class comisiones(models.Model):
    numero = models.CharField(max_length=30)
    clase = models.CharField(max_length=30)
