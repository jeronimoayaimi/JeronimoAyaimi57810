from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView


@login_required
def home(request):
    return render(request,"barberia/index.html")

@login_required
def clientes(request):
    return render(request,"barberia/clientes.html")




#______________________________________________________________________________________________________________________________________________________
#__________________________________________________________SUCURSAL___________________________________________________________________________________
@login_required
def sucursal(request):
    contexto = {"sucursal":Sucursal.objects.all()}
    return render(request,"barberia/sucursal.html",contexto) 


                 #________ SUCURSAL FORM________

@login_required
def sucursalForm(request):
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursalN = miForm.cleaned_data.get("nombreSucursal")
            sucursalD = miForm.cleaned_data.get("direccionSucursal")
            sucursalT = miForm.cleaned_data.get("telSucursal")
            sucursalH = miForm.cleaned_data.get("horariosSucursal")
            sucursal = Sucursal(nombreSucursal=sucursalN, direccionSucursal =sucursalD, telSucursal=sucursalT, horariosSucursal = sucursalH)
            sucursal.save()
            contexto = {"sucursal":Sucursal.objects.all()}
            return render(request,"barberia/sucursal.html",contexto) 
    else:
        miForm = SucursalForm()
    return render(request,"barberia/sucursalForm.html",{"form":miForm})

                #________ SUCURSAL UPDATE________

@login_required
def sucursalUpdate(request, id_sucursal):
    sucursal = Sucursal.objects.get(id= id_sucursal)
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursal.nombreSucursal = miForm.cleaned_data.get("nombreSucursal")
            sucursal.direccionSucursal = miForm.cleaned_data.get("direccionSucursal")
            sucursal.telSucursal = miForm.cleaned_data.get("telSucursal")
            sucursal.horariosSucursal = miForm.cleaned_data.get("horariosSucursal")
            sucursal.save()
            contexto = {"sucursal":Sucursal.objects.all()}
            return render(request,"barberia/sucursal.html",contexto) 
    else:
        miForm = SucursalForm(initial={
                                       "nombreSucursal":sucursal.nombreSucursal,
                                       "direccionSucursal":sucursal.direccionSucursal,
                                       "telSucursal":sucursal.telSucursal,
                                       "horariosSucursal":sucursal.horariosSucursal
                                       })
    return render(request,"barberia/sucursalForm.html",{"form":miForm})

                #________ SERVICIO DELETE________


@login_required
def sucursalDelete(request, id_sucursal):
    sucursal = Sucursal.objects.get(id=id_sucursal)
    sucursal.delete()
    contexto = {
                    "sucursal": Sucursal.objects.all(),
                    "mensaje": "Sucursal eliminada."
                }
    return render(request,"barberia/sucursal.html",contexto)




#______________________________________________________________________________________________________________________________________________________
#__________________________________________________________SERVICIOS___________________________________________________________________________________

@login_required
def servicios(request):
    contexto = {"servicios": Servicio.objects.all()}
    return render(request,"barberia/servicios.html",contexto) 

            #________ SERVICIO FORM________
               

@login_required
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

               #________ SERVICIO UPDATE________
               
@login_required
def servicioUpdate(request, id_servicio):
    servicio = Servicio.objects.get(id=id_servicio)
    if request.method == "POST":
        miForm = ServiciosForm(request.POST)
        if miForm.is_valid():
            servicio.nombre = miForm.cleaned_data.get("nombre")
            servicio.descripcion = miForm.cleaned_data.get("descripcion")
            servicio.precio = miForm.cleaned_data.get("precio")
            servicio.save()
            contexto = {"servicios": Servicio.objects.all()}
            return render(request,"barberia/servicios.html",contexto)
    else:
        miForm= ServiciosForm (initial={"nombre":servicio.nombre, "descripcion": servicio.descripcion, "precio": servicio.precio})
    return render(request, "barberia/serviciosForms.html", {"form":miForm})


                 #________ SERVICIO DELETE________

@login_required
def servicioDelete(request, id_servicio):
    servicio = Servicio.objects.get(id=id_servicio)
    servicio.delete()
    contexto = {
                    "servicios": Servicio.objects.all(),
                    "mensaje": "Servicio eliminado."
                }
    return render(request,"barberia/servicios.html",contexto)

 
#______________________________________________________________________________________________________________________________________________________
#_________________________________________________RESERVAS_____________________________________________________________________________________________

@login_required
def reservas(request):
    contexto ={"reservas": Reserva.objects.all()}
    return render(request,"barberia/reservas.html",contexto)

                  #________RESERVAS FORM________
    
@login_required
def reservaForms(request):
    if request.method == "POST":
        miForm = ReservaForm(request.POST)
        if miForm.is_valid():
            reservaNombre = miForm.cleaned_data.get("nombreCliente")
            reservaEmail = miForm.cleaned_data.get("emailCliente")
            reservaFecha = miForm.cleaned_data.get("fechaTurno")
            reservaHora = miForm.cleaned_data.get("horaTurno")
            estado = "confirmado" 
            reserva = Reserva(
                nombreCliente=reservaNombre,
                emailCliente=reservaEmail,
                fechaTurno=reservaFecha,
                horaTurno=reservaHora,
                estado=estado
            )
            reserva.save()
            contexto = {"reservas": Reserva.objects.all()}
            return render(request, "barberia/reservas.html", contexto)
    else:
        miForm = ReservaForm()
    return render(request, 'barberia/reservaForm.html', {"form": miForm})


                       #________RESERVAS UPDATE________
                       
@login_required
def reservaUpdate(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    if request.method == "POST":
        miForm = ReservaForm(request.POST)
        if miForm.is_valid():
            reserva.nombreCliente = miForm.cleaned_data.get("nombreCliente")
            reserva.emailCliente = miForm.cleaned_data.get("emailCliente")
            reserva.fechaTurno = miForm.cleaned_data.get("fechaTurno")
            reserva.horaTurno = miForm.cleaned_data.get("horaTurno")
            reserva.estado = 'confirmado'
            reserva.save()
            contexto = {"reservas": Reserva.objects.all()}
            return render(request,"barberia/reservas.html",contexto)
            
    else:
        miForm = ReservaForm(initial={"nombreCliente":reserva.nombreCliente, "emailCliente":reserva.emailCliente, "fechaTurno":reserva.fechaTurno, "horaTurno":reserva.horaTurno})
        return render(request, "barberia/reservaForm.html", {"form":miForm})

                         #________RESERVAS CANCEL________

@login_required
def reservaCancel(request, id_reserva):
    reserva = get_object_or_404 (Reserva, id=id_reserva)
    reserva.estado = 'cancelado'
    reserva.save()
    contexto = {
        "reservas": Reserva.objects.filter(estado__in=['cancelado', 'confirmado']),
        "mensaje": "La reserva ha sido cancelada exitosamente."
    }
    return render(request, "barberia/reservas.html", contexto)



                       #________RESERVAS DELETE________
                       
@login_required
def reservaDelete(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    reserva.delete()
    contexto = {
                    "reservas": Reserva.objects.all(),
                    "mensaje": "Reserva eliminada."
                }
    return render(request,"barberia/reservas.html",contexto)                    
            
#______________________________________________________________________________________________________________________________________________________
#_________________________________________________PROFESIONAL__________________________________________________________________________________________

@login_required
def profesionales(request):
    contexto = {"profesionales": Barbero.objects.all()}
    return render(request,"barberia/profesionales.html",contexto)

               #________ PROFESIONAL FORM________

@login_required
def profesionalForms(request):
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesionalNombre = miForm.cleaned_data.get("nombre")
            profesionalApellido = miForm.cleaned_data.get("apellido")
            profesionalEmail = miForm.cleaned_data.get("email")
            profesional = Barbero(nombre=profesionalNombre, apellido=profesionalApellido, email=profesionalEmail)
            profesional.save()
            contexto = {"profesionales": Barbero.objects.all()}
            return render(request, "barberia/profesionales.html", contexto)
    else:
        miForm = ProfesionalForm()
    return render(request, 'barberia/profesionalForm.html', {"form": miForm})


               #________ PROFESIONAL UPDATE________
               
@login_required
def profesionalUpdate(request, id_profesional):
    profesional = Barbero.objects.get(id=id_profesional)
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional.nombre = miForm.cleaned_data.get("nombre")
            profesional.apellido = miForm.cleaned_data.get("apellido")
            profesional.email = miForm.cleaned_data.get("email")
            profesional.save()
            contexto = {"profesionales": Barbero.objects.all()}
            return render(request, "barberia/profesionales.html", contexto)
    else:
        miForm = ProfesionalForm(initial={"nombre": profesional.nombre, "apellido": profesional.apellido, "email": profesional.email})
    return render(request, "barberia/profesionalForm.html", {"form": miForm})

         #________ PROFESIONAL DELETE________

@login_required
def profesionalDelete(request, id_profesional):
    profesional = Barbero.objects.get(id=id_profesional)
    profesional.delete()
    contexto = {
                    "profesionales": Barbero.objects.all(),
                    "mensaje": "Barbero eliminado."
                }
    return render(request, "barberia/profesionales.html", contexto)




#______________________________________________________________________________________________________________________________________________________
#______________________________________________________ BUSCADOR ______________________________________________________________________________________

@login_required
def buscarReserva(request):
    return render (request, "barberia/buscar.html")

@login_required
def encontrarReserva(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        reserva = Reserva.objects.filter(nombreCliente__icontains=patron)
        contexto = {'reservas': reserva}
        
    else:   
        contexto = {"reservas": Reserva.objects.all()}
    return render(request,"barberia/reservas.html",contexto)





#______________________________________________________________________________________________________________________________________________________
#_________________________________________________________________ LOGIN| REGISTER | LOGOUT ___________________________________________________________

def loginRequest (request): 
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username= usuario , password=clave)
        if user is not None:
            login(request, user)
            # Buscar Avatar
            try:
                avatar = Avatar.objects.get(user-request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
                
            return render (request, 'barberia/index.html')
        else: 
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    return render (request,"barberia/login.html", {"form" : miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForms(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = RegistroForms()  
    return render (request,"barberia/registro.html", {"form" : miForm})

#______________________________________________________________________________________________________________________________________________________
#_________________________________________________________________ EDITAR PERFIL - AVATAR _____________________________________________________________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = userEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = userEditForm(instance=usuario)
    return render(request, "barberia/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "barberia/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required
def agregar_avatar (request):
    usuario = request.user
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #borra avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range (len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario, imagen ="imagen")
            avatar.save()
            
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] =imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "barberia/agregarAvatar.html", {"form": miForm})
   