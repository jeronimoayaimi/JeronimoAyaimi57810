from django.contrib import admin

from .models import *

#___BARBERO
class  BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email')
    
admin.site.register(Barbero,BarberoAdmin)

#____ SERVICIO
class  ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    
admin.site.register(Servicio, ServicioAdmin)


admin.site.register(Cliente)
admin.site.register(Reserva)


