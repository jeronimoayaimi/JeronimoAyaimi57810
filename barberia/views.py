from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request,"barberia/index.html")

def servicios(request):
    contexto = {"servicios": Servicio.objects.all()}
    return render(request,"barberia/servicios.html",contexto) 

def clientes(request):
    return render(request,"barberia/clientes.html")

def profesionales(request):
    contexto = {"profesionales": Barbero.objects.all()}
    return render(request,"barberia/profesionales.html",contexto)

def reservas(request):
    contexto ={"reservas": Reserva.objects.all()}
    return render(request,"barberia/reservas.html",contexto)

#_____ Formularios

def serviciosForms(request):
    if request.method == "POST":
        miForm = ServiciosForm(request.POST)
        if miForm.is_valid():
            serviciosNombre = miForm.cleaned_data.get("nombre")
            serviciosDescripcion = miForm.cleaned_data.get("descripcion")
            serviciosPrecio = miForm.cleaned_data.get("precio")
            servicios = Servicio(nombre=serviciosNombre, descripcion = serviciosDescripcion, precio = serviciosPrecio)
            servicios.save()
            contexto = {"servicios": Servicio.objects.all()}
            return render(request,"barberia/servicios.html",contexto)
    else:
        miForm = ServiciosForm()
    
    return render (request, 'barberia/serviciosForms.html',{"form":miForm})



def reservaForms(request):
    if request.method == "POST":
        miForm = ReservaForm(request.POST)
        if miForm.is_valid():
            reservaNombre = miForm.cleaned_data.get("nombre")
            reservaEmail = miForm.cleaned_data.get("email")
            reservaFecha = miForm.cleaned_data.get("fechaTurno")
            reservaHora = miForm.cleaned_data.get("horaTurno")
            reserva = Reserva(nombreCliente=reservaNombre, emailCliente = reservaEmail, fechaTurno = reservaFecha, horaTurno = reservaHora)
            reserva.save()
            contexto = {"reservas": Reserva.objects.all()}
            return render(request,"barberia/reservas.html",contexto)
    else:
        miForm = ReservaForm()
    
    return render (request, 'barberia/reservaForm.html',{"form":miForm})




def profesionalForms(request):
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesionalNombre = miForm.cleaned_data.get("nombre")
            profesionalApellido = miForm.cleaned_data.get("apellido")
            profesionalEmail = miForm.cleaned_data.get("email")
            
            profesional = Barbero(nombre=profesionalNombre, apellido = profesionalApellido , email = profesionalApellido )
            profesional.save()
            contexto = {"profesionales": Barbero.objects.all()}
            return render(request,"barberia/profesionales.html",contexto)
    else:
        miForm = ProfesionalForm()
    
    return render (request, 'barberia/profesionalForm.html',{"form":miForm})


#________ Buscar

def buscarReserva(request):
    return render (request, "barberia/buscar.html")


def encontrarReserva(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        reserva = Reserva.objects.filter(nombreCliente__icontains=patron)
        contexto = {'reservas': reserva}
        
    else:   
        contexto = {"reservas": Reserva.objects.all()}
    return render(request,"barberia/reservas.html",contexto)