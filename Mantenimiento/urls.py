# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mantenimiento.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # include the lookup urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lookups/', include(ajax_select_urls)),
    url(r'^$','eventos.views.principal',name='principal'),
    url(r'^accesar/$','eventos.views.accesar', name='accesar'),
    url(r'^identificar/$','eventos.views.identificar', name='identificar'),
    url(r'^iniciar/$','eventos.views.iniciar', name='iniciar'),
    url(r'^salir/$','eventos.views.salir', name='salir'),
    url(r'^crear_orden/$','eventos.views.crear_orden', name='crear_orden'),
    url(r'^agregar_repuesto/$','eventos.views.agregar_parte_de_repuesto', name='agregar_repuesto'),
    url(r'^agregar_material_ocupado/$','eventos.views.agregar_material_ocupado', name='agregar_material_ocupado'),
    url(r'^modificar_orden/(?P<id>\d+)/$','eventos.views.modificar_orden', name='modificar_orden'),
    url(r'^add/m_MaterialesOcupados/?$', 'eventos.views.Nuevo_Material_Ocupado',name='Nuevo_Material_Ocupado'),
    url(r'^add/m_ParteDeRepuestoOcupada/?$', 'eventos.views.Nuevo_Repuesto_Ocupado',name='Nuevo_Material_Ocupado'),
    url(r'^generar_orden/(?P<id>\d+)/$','eventos.views.generar_orden', name='generar_orden'),


)
