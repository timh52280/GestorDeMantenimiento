# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.core.context_processors import csrf
from django.contrib.auth import *
from .forms import *
from .models import Orden_Mantenimiento
from django.contrib import messages
from django.utils.html import escape
from django.contrib.auth.decorators import login_required


def graph(request):
    import random
    import django
    import datetime
    import time
    
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    
    
    instances = Orden_Mantenimiento.objects.all()
    timestamps = []
    for instance in instances:
        timestamps.append(instance.m_FechaHoraCreacion)
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[1,2,3,4,5,6]
    y=[2,4,6,8,10,12]
    
    ax.plot(x, y)
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
      