from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ServiciosForm(forms.Form):
    nombre      = forms.CharField(max_length=60, required=True)
    descripcion = forms.CharField(max_length=60, required=True)
    precio = forms.CharField(max_length=60, required=True)
    
    
class ProfesionalForm(forms.Form):
    nombre      = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    
    
class ReservaForm(forms.Form):
    nombreCliente = forms.CharField(max_length=100, required=True, label='Nombre')
    emailCliente = forms.EmailField(required=True, label='Email')
    fechaTurno = forms.DateField(label='Fecha del turno')
    horaTurno = forms.TimeField(label='Hora del turno')
    


        

class SucursalForm(forms.Form):
    nombreSucursal = forms.CharField(max_length=100, required=True, label= 'Sucursal')
    direccionSucursal = forms.CharField(max_length=100, required=True, label ='Direccion')
    telSucursal =  forms.CharField(max_length=100, required=True, label = 'Telefono')
    horariosSucursal =  forms.CharField(max_length=100, required=True, label = 'Horarios')


class RegistroForms(UserCreationForm):
    first_name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class userEditForm(UserChangeForm): 
    first_name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    