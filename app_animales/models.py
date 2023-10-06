from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"Cuidador: {self.cuidador}, Nombre: {self.nombre}, Tipo: {self.tipo}"

class Protectora(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Protectora: {self.nombre} Descripción: {self.descripcion}, Fecha creacion: {self.fecha_creacion}"
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    fecha_entrada_protectora = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Colaborador: {self.nombre}, Cargo: {self.cargo}, Fecha de ingreso: {self.fecha_entrada_protectora}"