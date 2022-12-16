from django.db import models
from datetime import datetime

# Create your models here.
class seminario(models.Model) :
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechaIns = models.DateField()
    horaIns = models.TimeField()
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)