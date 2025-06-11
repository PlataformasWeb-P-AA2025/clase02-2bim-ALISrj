from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s - edad: %d" % (self.nombre,
                                            self.apellido,
                                            self.cedula,
                                            self.edad)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    poblacion = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.nombre, self.poblacion)