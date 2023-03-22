from django.db import models

# Create your models here.

class Pet(models.Model):
    id = models.CharField(verbose_name="Identificador Único", max_length=255)
    name = models.CharField(verbose_name="Nombre", max_length=255)
    race = models.CharField(verbose_name="Raza", max_length=255)
    gender = models.CharField(verbose_name="Sexo", max_length=255)
    origin = models.CharField(verbose_name="Pais de Origen", max_length=255)
    color = models.CharField(verbose_name="Color", max_length=255)
    user = models.CharField(verbose_name="Usuario", max_length=255)

