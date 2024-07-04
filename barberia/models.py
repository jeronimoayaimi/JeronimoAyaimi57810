from django.db import models

# Modelo de datos de la App Barberia

class Barbero (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
class Reserva(models.Model):
    nombreCliente = models.CharField(max_length=100)
    emailCliente = models.EmailField()
    fechaTurno = models.DateField()
    horaTurno = models.TimeField()
    
    
    