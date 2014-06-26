# -*- coding: utf-8 -*-
from django.forms import ModelForm,ValidationError
from django.contrib.auth.models import *
from django import forms
from datetime import datetime
from django.contrib.admin import widgets
from django.template.loader import render_to_string
from .models import *
from ajax_select import make_ajax_field
from ajax_select.fields import *


class SelectWithPop(forms.Select):
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("popupplus.html", {'field': name})
        return html+popupplus

class MultipleSelectWithPop(forms.SelectMultiple):
    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("popupplus.html", {'field': name})
        return html+popupplus

class Orden_Mantenimiento_Form(forms.ModelForm):
    
    m_TipoTrabajo = forms.ModelChoiceField(queryset=Tipo_Trabajo.objects.all(), widget=forms.RadioSelect(),empty_label=None,label = "Tipo de trabajo a realizar")  
    m_TipoMantenimiento = forms.ModelChoiceField(queryset=Tipo_Mantenimiento.objects.all(), widget=forms.RadioSelect(),empty_label = None,label = "Tipo de mantenimiento a realizar")
    m_Equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(), widget=forms.Select(),empty_label="Seleccione un equipo...",required=False ,label = "Equipo donde se realizara el trabajo de mantenimiento")
    m_Descripcion = forms.CharField(widget=forms.Textarea(),label="Escriba una breve descripción del trabajo a realizar")
    m_Prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.all(), widget=forms.Select(),empty_label = "Seleccione la prioridad...", label = "¿Qué prioridad tiene el trabajo de mantenimiento?")
    m_PartesDeRepuestoOcupadas = AutoCompleteSelectField('partederepuesto', required=False, help_text=None)
    m_FechaHoraCreacion = models.DateTimeField(auto_now_add=True)    
    m_CodigosdeCausa = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(), queryset=CodigoCausa.objects.all(),required=False,label='Códigos de causa que originaron el mantenimiento')     
    m_Supervisor = AutoCompleteSelectField('supervisor', required=False, help_text=None) 
    m_Personal = AutoCompleteSelectMultipleField('personal', required=False, help_text=None)   
    m_Programable = forms.BooleanField(label="Active la casilla si esta orden puede ser agregada al programa de mantenimiento preventivo.")    
    def __init__(self,*args,**kwargs):
        super (Orden_Mantenimiento_Form,self ).__init__(*args,**kwargs)      
        
    class Meta:
        model = Orden_Mantenimiento
        
class ParteDeRepuesto_Form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (ParteDeRepuesto_Form,self ).__init__(*args,**kwargs)      
        
    class Meta:
        model = ParteDeRepuestoOcupada
        
class Material_Ocupado_Form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (Material_Ocupado_Form,self ).__init__(*args,**kwargs)      
        
    class Meta:
        model = MaterialOcupado
        