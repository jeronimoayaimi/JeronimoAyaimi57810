from django import forms 

class ServiciosForm(forms.Form):
    nombre      = forms.CharField(max_length=60, required=True)
    descripcion = forms.CharField(max_length=60, required=True)
    precio = forms.CharField(max_length=60, required=True)
    
    
class ProfesionalForm(forms.Form):
    nombre      = forms.CharField(max_length=60, required=True)
    apellido = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    
    
class ReservaForm(forms.Form):
    nombre      = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    fechaTurno = forms.DateField( label = 'Fecha turno')
    horaTurno = forms.TimeField(label = 'Hora turno')
    