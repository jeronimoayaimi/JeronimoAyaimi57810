from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = "home"),
    path('clientes/', clientes, name = "clientes"),
    
    
    #_________________________________________________PROFESIONALES________________________________________________________
    
     path('profesionales/', profesionales, name = "profesionales"),
     path('profesionalForm/', profesionalForms, name = "profesionalForm"),
     path('profesionalUpdate/<id_profesional>', profesionalUpdate, name = "profesionalUpdate"),
     path('profesionalDelete/<id_profesional>', profesionalDelete, name = "profesionalDelete"),
    
    #_________________________________________________RESERVAS____________________________________________________________
    
    path('reservas/', reservas, name = "reservas"),
    path('reservaForm/', reservaForms, name = "reservaForm"),
    path('buscarReserva/', buscarReserva, name = "buscarReserva"),
    path('encontrarReserva/', encontrarReserva, name = "encontrarReserva"),
    path ('reservaUpdate/<id_reserva>', reservaUpdate, name= 'reservaUpdate'),
    path ('reservaCancel/<id_reserva>', reservaCancel, name= 'reservaCancel'),
    path ('reservaDelete/<id_reserva>', reservaDelete, name= 'reservaDelete'),
 
    
   #_________________________________________________SERVICIOS____________________________________________________________
    path('servicios/', servicios, name = "servicios"),
    path('serviciosForms/', serviciosForms, name = "serviciosForm"),
    path('serviciosUpdate/<id_servicio>', servicioUpdate, name = "serviciosUpdate"),
    path('serviciosDelete/<id_servicio>', servicioDelete, name = "serviciosDelete"),
    
    #_________________________________________________SUCURSAL____________________________________________________________
    path('sucursal/', sucursal, name = "sucursal"),
    path('sucursalForms/', sucursalForm, name = "sucursalForm"),
    path('sucursalUpdate/<id_sucursal>', sucursalUpdate, name = "sucursalUpdate"),
    path('sucursalDelete/<id_sucursal>', sucursalDelete, name = "sucursalDelete"),
    
    #______________________________________ LOGIN| REGISTER | LOGOUT_____________________________________________________
    
    path('login/', loginRequest, name = "login"),
    path('logout/', LogoutView.as_view(template_name="barberia/logout.html"), name="logout"),
    path('registro/', register,  name='registro'),
    
    #______________________________________ EDITAR PERFIL | AVATAR ______________________________________________________
    
    path('perfil', editProfile, name='perfil'),
    path('<int:pk>/password/', CambiarClave.as_view(), name='cambiarClave'),
    path('agregarAvatar', agregar_avatar, name='agregarAvatar'),

]