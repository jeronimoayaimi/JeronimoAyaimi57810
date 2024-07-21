from django.db import models
from django.contrib.auth.models import User


# Modelo de datos de la App Barberia

class Barbero (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nombre, self.apellido}'
    
class Reserva(models.Model):
    nombreCliente = models.CharField(max_length=100)
    emailCliente = models.EmailField()
    fechaTurno = models.DateField()
    horaTurno = models.TimeField()
    estado = [
                ('confirmado','Confirmado'),
                ('cancelado','Cancelado'),        
              ]
    
    estado = models.CharField(max_length=10, choices=estado, default='Confirmado')
    
    def __str__(self):
        return f'{self.nombreCliente}'
    
class Sucursal(models.Model):
    nombreSucursal = models.CharField(max_length=100)
    direccionSucursal = models.CharField(max_length=100)
    telSucursal =  models.CharField(max_length=100)
    horariosSucursal =  models.CharField(max_length=100)
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} {self.imagen}'