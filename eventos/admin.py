# -*- coding: utf-8 -*-
from django.contrib import admin
from eventos.models import *

admin.site.register(Mes)
admin.site.register(Mantenimiento_Categoria)
admin.site.register(Denominacion)
admin.site.register(Equipo)
admin.site.register(Prioridad)
admin.site.register(CodigoCausa)
admin.site.register(CodigoColor)
admin.site.register(CategoriaMaterial)
admin.site.register(Material)
admin.site.register(MaterialOcupado)
admin.site.register(ParteDeRepuesto)
admin.site.register(ParteDeRepuestoOcupada)
admin.site.register(Evento_Mantenimiento)
admin.site.register(Mantenimiento_Programado)
admin.site.register(Tipo_Trabajo)
admin.site.register(Tipo_Mantenimiento)
admin.site.register(Orden_Mantenimiento)
admin.site.register(Mantenimiento_Verificado)
admin.site.register(Mantenimiento_Validado)
admin.site.register(Bitacora_Mantenimiento)

