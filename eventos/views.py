# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.core.context_processors import csrf
from django.contrib.auth import *
from .forms import *
from .models import Orden_Mantenimiento
from django.contrib import messages
from django.utils.html import escape
from django.contrib.auth.decorators import login_required
from numpy import *
def generar_error(request,error_id):
    pass

def crear_bitacora(request,orden):
    instance = Orden_Mantenimiento.objects.get(pk=orden)
    if len(Bitacora_Mantenimiento.objects.filter(m_OrdenMantenimiento__pk=orden)) != None:
        return HttpResponseRedirect("/error/250/")
    if request.POST:
        form = Bitacora_Mantenimiento_Form(request.POST,initial={'m_OrdenMantenimiento':instance},orden_id=instance.pk,usuario=request.user)
        if form.is_valid():
            data=form.save()
            return HttpResponseRedirect("/generar_orden/%s/" % (data.m_ID))
    else:
        form = Bitacora_Mantenimiento_Form(initial={'m_OrdenMantenimiento':instance},usuario=request.user,orden_id=instance.pk)
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                # Ignore unexpected parameters
                pass
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['instance'] = instance
 
    return render_to_response('crear_bitacora_mantenimiento.html', args)

def estadisticas(request,anyo_id):
    args = {}
    args['anyo_id'] = anyo_id
    args.update(csrf(request))
    return render_to_response("estadisticas.html", args)

def graph_anual(request,anyo_id):
    import random
    import django
    import datetime
    import time
    
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    
    instances_p = Orden_Mantenimiento.objects.filter(m_TipoMantenimiento=1,m_FechaHoraCreacion__year=anyo_id)
    instances_c = Orden_Mantenimiento.objects.filter(m_TipoMantenimiento=2,m_FechaHoraCreacion__year=anyo_id)
    meses = (1,2,3,4,5,6,7,8,9,10,11,12)
    meses_labels = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
    mantenimientos_p = [0,0,0,0,0,0,0,0,0,0,0,0]
    mantenimientos_c = [0,0,0,0,0,0,0,0,0,0,0,0]
    timestamps = []
    for instance in instances_p:
        if instance.m_FechaHoraCreacion.month == 1:
            mantenimientos_p[0] += 1
        if instance.m_FechaHoraCreacion.month == 2:
            mantenimientos_p[1] += 1
        if instance.m_FechaHoraCreacion.month == 3:
            mantenimientos_p[2] += 1
        if instance.m_FechaHoraCreacion.month == 4:
            mantenimientos_p[3] += 1
        if instance.m_FechaHoraCreacion.month == 5:
            mantenimientos_p[4] += 1
        if instance.m_FechaHoraCreacion.month == 6:
            mantenimientos_p[5] += 1
        if instance.m_FechaHoraCreacion.month == 7:
            mantenimientos_p[6] += 1
        if instance.m_FechaHoraCreacion.month == 8:
            mantenimientos_p[7] += 1
        if instance.m_FechaHoraCreacion.month == 9:
            mantenimientos_p[8] += 1
        if instance.m_FechaHoraCreacion.month == 10:
            mantenimientos_p[9] += 1
        if instance.m_FechaHoraCreacion.month == 11:
            mantenimientos_p[10] += 1
        if instance.m_FechaHoraCreacion.month == 12:
            mantenimientos_p[11] += 1
            
            
    for instance in instances_c:
        if instance.m_FechaHoraCreacion.month == 1:
            mantenimientos_c[0] += 1
        if instance.m_FechaHoraCreacion.month == 2:
            mantenimientos_c[1] += 1
        if instance.m_FechaHoraCreacion.month == 3:
            mantenimientos_c[2] += 1
        if instance.m_FechaHoraCreacion.month == 4:
            mantenimientos_c[3] += 1
        if instance.m_FechaHoraCreacion.month == 5:
            mantenimientos_c[4] += 1
        if instance.m_FechaHoraCreacion.month == 6:
            mantenimientos_c[5] += 1
        if instance.m_FechaHoraCreacion.month == 7:
            mantenimientos_c[6] += 1
        if instance.m_FechaHoraCreacion.month == 8:
            mantenimientos_c[7] += 1
        if instance.m_FechaHoraCreacion.month == 9:
            mantenimientos_c[8] += 1
        if instance.m_FechaHoraCreacion.month == 10:
            mantenimientos_c[9] += 1
        if instance.m_FechaHoraCreacion.month == 11:
            mantenimientos_c[10] += 1
        if instance.m_FechaHoraCreacion.month == 12:
            mantenimientos_c[11] += 1
            
    fig=Figure()
    ax=fig.add_subplot(111)
    
    ax.bar(array(meses)-0.2 , mantenimientos_p, width=0.4 ,color = 'green', align='center' )
    ax.bar( array(meses)+0.2, mantenimientos_c, width=0.4 , color = 'red', align='center')
    
    ax.set_title(u'Ordenes de Mantenimiento Año %s' % (anyo_id,))
    ax.set_ylabel('Ordenes de Mantenimiento Elaboradas')
    ax.set_xlabel(u'Año 2014')
    ax.legend(('M. Preventivo', 'M. Correctivo'), 'upper right', shadow=True)
    
    ax.set_xticks(meses)
    ax.set_xticklabels(meses_labels)
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def mantenimiento_anual(request):
    args = {}
    args.update(csrf(request))
    return render_to_response("mantenimiento_anual.html", args)

def ver_ordenes(request):
    instance = Orden_Mantenimiento.objects.all().order_by('pk')
    args = {}
    args.update(csrf(request))
    
    args['instance'] = instance
    return render_to_response("ver_ordenes.html", args)

def generar_orden(request,id):
    instance = Orden_Mantenimiento.objects.get(pk=id)
    args = {}
    args.update(csrf(request))
    
    args['instance'] = instance
    return render_to_response("generar_orden.html", args)

def handlePopAdd(request, addForm, field):

    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError:
                newObject = None
            if newObject:
                return HttpResponse('<!DOCTYPE html><html><head><title></title></head><body><script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script></body></html>' % (escape(newObject._get_pk_val()), escape(newObject)))
    else:
        form = addForm()
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['field'] = field
 
    return render_to_response("popadd.html", args)

def Nuevo_Repuesto_Ocupado(request):
    return handlePopAdd(request, ParteDeRepuesto_Form, 'm_ParteDeRepuestoOcupada')

def Nuevo_Material_Ocupado(request):
    return handlePopAdd(request, Material_Ocupado_Form, 'm_MaterialesOcupados')

def principal(request):
    user = request.user
    groups = user.groups.all()
    
    personal_group = groups.filter(name='personal')
    supervisor_group = groups.filter(name='supervisores')
    validador_group = groups.filter(name='validadores')
    
    if (personal_group.exists()):
        return render(request,'personal.html',{'user':user,'group':personal_group[0],})
    elif (supervisor_group.exists()):
        return render(request,'supervisor.html',{'user':user,'group':supervisor_group[0],})
    elif (validador_group.exists()):
        return render(request,'validador.html',{'user':user,'group':validador_group[0],})
    else:
        return render(request,'error_acceso.html',{})

def identificar(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=authenticate(username=username,password=password)
    
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/iniciar/')
    else:
        return render(request,'error_acceso.html',{})


def accesar(request):
    c={}
    c.update(csrf(request))
    return render(request,"identificar.html",c)


def iniciar(request):
    user = request.user
    groups = user.groups.all()
    
    personal_group = groups.filter(name='personal')
    supervisor_group = groups.filter(name='supervisores')
    validador_group = groups.filter(name='validadores')
    
    if (personal_group.exists()):
        return render(request,'personal.html',{'user':user,'group':personal_group[0],})
    elif (supervisor_group.exists()):
        return render(request,'supervisor.html',{'user':user,'group':supervisor_group[0],})
    elif (validador_group.exists()):
        return render(request,'validador.html',{'user':user,'group':validador_group[0],})
    else:
        return render(request,'error_acceso.html',{})
        
def salir(request):
    logout(request)
    return render_to_response('salir.html',{},context_instance=RequestContext(request))
    
def generar_mantenimientos_programados(anyo):
    return
@login_required 
def crear_orden(request):
    if request.POST:
        form = Orden_Mantenimiento_Form(request.POST)
        if form.is_valid():
            data = form.save()
 
            return HttpResponseRedirect("/generar_orden/%s/" % (data.m_ID))
    else:
        form = Orden_Mantenimiento_Form()
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                # Ignore unexpected parameters
                pass
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('crear_orden_mantenimiento.html', args)
    
    
def agregar_parte_de_repuesto(request):
    if request.POST:
        form = ParteDeRepuesto_Form(request.POST)
        if form.is_valid():
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = ParteDeRepuesto_Form()
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                # Ignore unexpected parameters
                pass
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('agregar_parte_de_repuesto.html', args)

def agregar_material_ocupado(request):
    if request.POST:
        form = Material_Ocupado_Form(request.POST)
        if form.is_valid():
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = Material_Ocupado_Form()
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                # Ignore unexpected parameters
                pass
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('agregar_material_ocupado.html', args)
    
    
def modificar_orden(request,id=None):
    object_instance = get_object_or_404(Orden_Mantenimiento, pk=id)
    if request.POST:
        form = Orden_Mantenimiento_Form(request.POST,instance=object_instance)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, _('Orden de mantenimiento guardada correctamente.'))
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = Orden_Mantenimiento_Form(instance=object_instance)
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('modificar_orden_mantenimiento.html', args)
      