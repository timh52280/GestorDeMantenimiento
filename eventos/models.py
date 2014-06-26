# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mes(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.m_Nombre

class Mantenimiento_Categoria(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Abreviatura = models.CharField(max_length=3)
    m_Descripcion = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.m_Descripcion

class Denominacion(models.Model):
     m_ID = models.AutoField(primary_key=True)
     m_Denominacion = models.CharField(max_length=50)
     
     def __unicode__(self):
        return self.m_Denominacion

class Equipo(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre = models.CharField(max_length=250)
    m_Modelo = models.CharField(max_length=250)
    m_Fabricante = models.CharField(max_length=250)
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.m_Nombre,self.m_Fabricante,self.m_Modelo)
        
class Prioridad(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.m_Nombre

class CodigoCausa(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Causa = models.CharField(max_length=250)
    
    def __unicode__(self):
        return u'%s - %s' % (self.m_ID,self.m_Causa)

class CodigoColor(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Color = models.CharField(max_length=250)
    m_ActividadRelacionada = models.CharField(max_length=250)
    
    def __unicode__(self):
        return u'%s - %s' % (self.m_Color,self.m_ActividadRelacionada)
        
class CategoriaMaterial(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_NombreCategoria = models.CharField(max_length=250)
    m_CodigoColor = models.ForeignKey(CodigoColor,max_length=250)
    
    def __unicode__(self):
        return self.m_NombreCategoria

class Material(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Articulo = models.CharField(max_length=100)
    m_Descripcion = models.CharField(max_length=100)
    m_CategoriaMaterial = models.ForeignKey(CategoriaMaterial,related_name = 'Denominacion')
    m_FechaCompra = models.DateField()
    m_Proveedor = models.CharField(max_length=100)
    m_PrecioCompra = models.CharField(max_length=20)
    m_Stock = models.IntegerField()
    m_Denominacion = models.ForeignKey(Denominacion)
    
    def __unicode__(self):
        return self.m_Descripcion

class ParteDeRepuesto(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Articulo = models.CharField(max_length=250)
    m_Descripcion = models.CharField(max_length=250)
    m_Marca = models.CharField(max_length=250)
    m_Modelo = models.CharField(max_length=250)
    m_Equipo = models.ForeignKey(Equipo,related_name = 'EquipoMantenimiento')
    m_PrecioUnitario = models.FloatField()
    m_Proveedor = models.CharField(max_length=100)
    m_TotalEnStock = models.FloatField()
    m_FechaCompra = models.DateField()
    
    def __unicode__(self):
        return self.m_Articulo + self.m_Marca + self.m_Modelo
        
class MaterialOcupado(models.Model):
    m_Material = models.ForeignKey(Material,related_name = 'Material')
    m_CantidadAOcupar = models.FloatField()
    m_Denominacion = models.ForeignKey(Denominacion,related_name = 'Denominacion')
    
    def __unicode__(self):
        return self.m_Material.m_Articulo
        
class ParteDeRepuestoOcupada(models.Model):
    m_Parte = models.ForeignKey(ParteDeRepuesto,related_name = 'Parte_Repuesto')
    m_CantidadAOcupar = models.FloatField()
    m_Denominacion = models.ForeignKey(Denominacion,related_name = 'Denominacion_Parte')
    
    def __unicode__(self):
        return str(self.m_CantidadAOcupar) + " " + str(self.m_Denominacion) + " " + str(self.m_Parte.m_Articulo)

class Evento_Mantenimiento(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre=models.CharField(max_length=255)
    m_Descripcion=models.CharField(max_length=255,null=True,blank=True)
    m_Categoria=models.ForeignKey(Mantenimiento_Categoria)
    m_Frecuencia_meses=models.IntegerField()
    m_MesInicio=models.ForeignKey(Mes)
    m_AnyoIinicio=models.IntegerField()

    def __unicode__(self):
        return self.m_Nombre
        
class Mantenimiento_Programado(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_EventoMantenimiento=models.ForeignKey(Evento_Mantenimiento)
    m_Mes=models.ForeignKey(Mes)
    m_Anyo=models.IntegerField()

    def __unicode__(self):
        return self.m_EventoMantenimiento.m_Nombre

class Tipo_Trabajo(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.m_Nombre

class Tipo_Mantenimiento(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_Nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.m_Nombre

class Orden_Mantenimiento(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_TipoTrabajo = models.ForeignKey(Tipo_Trabajo,related_name = 'Tipo_Trabajo')
    m_TipoMantenimiento = models.ForeignKey(Tipo_Mantenimiento,related_name = 'Tipo_Mantenimiento')
    m_Equipo = models.ForeignKey(Equipo,related_name = 'Equipo',blank=True,null=True)
    m_Descripcion = models.CharField(max_length=500)    
    m_Prioridad = models.ForeignKey(Prioridad,related_name = 'Prioridad')
    m_PartesDeRepuestoOcupadas = models.ManyToManyField(ParteDeRepuestoOcupada, related_name = 'Piezas_Repuesto_Ocupadas',blank=True,null=True)    
    m_MaterialesOcupados = models.ManyToManyField(MaterialOcupado, related_name = 'Materiales_Ocupados',blank=True,null=True)
    m_FechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    m_FechaHoraCompletado = models.DateTimeField(null=True,blank=True)
    m_FechaHoraMantAnt = models.DateTimeField(null=True,blank=True)
    m_CodigosdeCausa =  models.ManyToManyField(CodigoCausa, related_name = 'Codigos_Causas',blank=True) 
    m_CostoTotal = models.FloatField(null=True, blank=True)
    m_Supervisor = models.ForeignKey(User,related_name = 'Supervisor')      
    m_Personal=models.ManyToManyField(User, related_name = 'Personal')
    m_Programable = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'Número de orden: ' + u'%d' % self.m_ID
        
class Mantenimiento_Verificado(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_MantenimientoProgramado = models.ForeignKey(Mantenimiento_Programado)
    m_Verificado = models.BooleanField()
    m_VerificadoPor = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.m_MantenimientoProgramado.m_EventoMantenimiento.m_Nombre
        
class Mantenimiento_Validado(models.Model):
     m_ID = models.AutoField(primary_key=True)
     m_MantenimientoProgramado = models.ForeignKey(Mantenimiento_Programado)
     m_Validado = models.BooleanField()
     m_ValidadoPor = models.ForeignKey(User)
     
     def __unicode__(self):
        return self.m_MantenimientoProgramado.m_EventoMantenimiento.m_Nombre
        
class Bitacora_Mantenimiento(models.Model):
    m_ID = models.AutoField(primary_key=True)
    m_FechaHora = models.DateTimeField(auto_now_add=True)
    m_OrdenMantenimiento = models.ForeignKey(Orden_Mantenimiento)
    m_ProblemaParo = models.CharField(max_length=500,null=True,blank=True)
    m_AccionRealizada = models.CharField(max_length=500)
    m_Observaciones = models.CharField(max_length=500)
    m_Personal = models.ForeignKey(User,null=True,blank=True)
    m_HoraInicio = models.TimeField()
    m_HoraFin = models.TimeField()
    
    def __unicode__(self):
        return self.m_OrdenMantenimiento.m_MantenimientoProgramado.m_EventoMantenimiento.m_Nombre