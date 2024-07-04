from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('clientes/', clientes, name = "clientes"),
    path('servicios/', servicios, name = "servicios"),
    path('profesionales/', profesionales, name = "profesionales"),
    path('reservas/', reservas, name = "reservas"),
    
    #________Formularios
    path('serviciosForms/', serviciosForms, name = "serviciosForm"),
    path('reservaForm/', reservaForms, name = "reservaForm"),
    path('profesionalForm/', profesionalForms, name = "profesionalForm"),
    
    path('buscarReserva/', buscarReserva, name = "buscarReserva"),
    path('encontrarReserva/', encontrarReserva, name = "encontrarReserva"),
    
    
  
]