# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mes'
        db.create_table(u'eventos_mes', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'eventos', ['Mes'])

        # Adding model 'Mantenimiento_Categoria'
        db.create_table(u'eventos_mantenimiento_categoria', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Abreviatura', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('m_Descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'eventos', ['Mantenimiento_Categoria'])

        # Adding model 'Denominacion'
        db.create_table(u'eventos_denominacion', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Denominacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'eventos', ['Denominacion'])

        # Adding model 'Equipo'
        db.create_table(u'eventos_equipo', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Modelo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Fabricante', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'eventos', ['Equipo'])

        # Adding model 'Prioridad'
        db.create_table(u'eventos_prioridad', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'eventos', ['Prioridad'])

        # Adding model 'CodigoCausa'
        db.create_table(u'eventos_codigocausa', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Causa', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'eventos', ['CodigoCausa'])

        # Adding model 'CodigoColor'
        db.create_table(u'eventos_codigocolor', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Color', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_ActividadRelacionada', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'eventos', ['CodigoColor'])

        # Adding model 'CategoriaMaterial'
        db.create_table(u'eventos_categoriamaterial', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_NombreCategoria', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_CodigoColor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.CodigoColor'], max_length=250)),
        ))
        db.send_create_signal(u'eventos', ['CategoriaMaterial'])

        # Adding model 'Material'
        db.create_table(u'eventos_material', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Articulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('m_Descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('m_CategoriaMaterial', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Denominacion', to=orm['eventos.CategoriaMaterial'])),
            ('m_FechaCompra', self.gf('django.db.models.fields.DateField')()),
            ('m_Proveedor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('m_PrecioCompra', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('m_Stock', self.gf('django.db.models.fields.IntegerField')()),
            ('m_Denominacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Denominacion'])),
        ))
        db.send_create_signal(u'eventos', ['Material'])

        # Adding model 'ParteDeRepuesto'
        db.create_table(u'eventos_partederepuesto', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Articulo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Descripcion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Marca', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Modelo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('m_Equipo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='EquipoMantenimiento', to=orm['eventos.Equipo'])),
            ('m_PrecioUnitario', self.gf('django.db.models.fields.FloatField')()),
            ('m_Proveedor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('m_TotalEnStock', self.gf('django.db.models.fields.FloatField')()),
            ('m_FechaCompra', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'eventos', ['ParteDeRepuesto'])

        # Adding model 'MaterialOcupado'
        db.create_table(u'eventos_materialocupado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Material', to=orm['eventos.Material'])),
            ('m_CantidadAOcupar', self.gf('django.db.models.fields.FloatField')()),
            ('m_Denominacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Denominacion', to=orm['eventos.Denominacion'])),
        ))
        db.send_create_signal(u'eventos', ['MaterialOcupado'])

        # Adding model 'ParteDeRepuestoOcupada'
        db.create_table(u'eventos_partederepuestoocupada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Parte', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Parte_Repuesto', to=orm['eventos.ParteDeRepuesto'])),
            ('m_CantidadAOcupar', self.gf('django.db.models.fields.FloatField')()),
            ('m_Denominacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Denominacion_Parte', to=orm['eventos.Denominacion'])),
        ))
        db.send_create_signal(u'eventos', ['ParteDeRepuestoOcupada'])

        # Adding model 'Evento_Mantenimiento'
        db.create_table(u'eventos_evento_mantenimiento', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('m_Descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('m_Categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Mantenimiento_Categoria'])),
            ('m_Frecuencia_meses', self.gf('django.db.models.fields.IntegerField')()),
            ('m_MesInicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Mes'])),
            ('m_AnyoIinicio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'eventos', ['Evento_Mantenimiento'])

        # Adding model 'Mantenimiento_Programado'
        db.create_table(u'eventos_mantenimiento_programado', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_EventoMantenimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento_Mantenimiento'])),
            ('m_Mes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Mes'])),
            ('m_Anyo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'eventos', ['Mantenimiento_Programado'])

        # Adding model 'Tipo_Trabajo'
        db.create_table(u'eventos_tipo_trabajo', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'eventos', ['Tipo_Trabajo'])

        # Adding model 'Tipo_Mantenimiento'
        db.create_table(u'eventos_tipo_mantenimiento', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'eventos', ['Tipo_Mantenimiento'])

        # Adding model 'Orden_Mantenimiento'
        db.create_table(u'eventos_orden_mantenimiento', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_TipoTrabajo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Tipo_Trabajo', to=orm['eventos.Tipo_Trabajo'])),
            ('m_TipoMantenimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Tipo_Mantenimiento', to=orm['eventos.Tipo_Mantenimiento'])),
            ('m_Equipo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Equipo', null=True, to=orm['eventos.Equipo'])),
            ('m_Descripcion', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('m_Prioridad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Prioridad', to=orm['eventos.Prioridad'])),
            ('m_FechaHoraCreacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('m_FechaHoraCompletado', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('m_FechaHoraMantAnt', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('m_CostoTotal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('m_Supervisor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Supervisor', to=orm['auth.User'])),
            ('m_Programable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'eventos', ['Orden_Mantenimiento'])

        # Adding M2M table for field m_PartesDeRepuestoOcupadas on 'Orden_Mantenimiento'
        m2m_table_name = db.shorten_name(u'eventos_orden_mantenimiento_m_PartesDeRepuestoOcupadas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orden_mantenimiento', models.ForeignKey(orm[u'eventos.orden_mantenimiento'], null=False)),
            ('partederepuestoocupada', models.ForeignKey(orm[u'eventos.partederepuestoocupada'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orden_mantenimiento_id', 'partederepuestoocupada_id'])

        # Adding M2M table for field m_MaterialesOcupados on 'Orden_Mantenimiento'
        m2m_table_name = db.shorten_name(u'eventos_orden_mantenimiento_m_MaterialesOcupados')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orden_mantenimiento', models.ForeignKey(orm[u'eventos.orden_mantenimiento'], null=False)),
            ('materialocupado', models.ForeignKey(orm[u'eventos.materialocupado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orden_mantenimiento_id', 'materialocupado_id'])

        # Adding M2M table for field m_CodigosdeCausa on 'Orden_Mantenimiento'
        m2m_table_name = db.shorten_name(u'eventos_orden_mantenimiento_m_CodigosdeCausa')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orden_mantenimiento', models.ForeignKey(orm[u'eventos.orden_mantenimiento'], null=False)),
            ('codigocausa', models.ForeignKey(orm[u'eventos.codigocausa'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orden_mantenimiento_id', 'codigocausa_id'])

        # Adding M2M table for field m_Personal on 'Orden_Mantenimiento'
        m2m_table_name = db.shorten_name(u'eventos_orden_mantenimiento_m_Personal')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orden_mantenimiento', models.ForeignKey(orm[u'eventos.orden_mantenimiento'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orden_mantenimiento_id', 'user_id'])

        # Adding model 'Mantenimiento_Verificado'
        db.create_table(u'eventos_mantenimiento_verificado', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_MantenimientoProgramado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Mantenimiento_Programado'])),
            ('m_Verificado', self.gf('django.db.models.fields.BooleanField')()),
            ('m_VerificadoPor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'eventos', ['Mantenimiento_Verificado'])

        # Adding model 'Mantenimiento_Validado'
        db.create_table(u'eventos_mantenimiento_validado', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_MantenimientoProgramado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Mantenimiento_Programado'])),
            ('m_Validado', self.gf('django.db.models.fields.BooleanField')()),
            ('m_ValidadoPor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'eventos', ['Mantenimiento_Validado'])

        # Adding model 'Bitacora_Mantenimiento'
        db.create_table(u'eventos_bitacora_mantenimiento', (
            ('m_ID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('m_FechaHora', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('m_OrdenMantenimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Orden_Mantenimiento'])),
            ('m_ProblemaParo', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('m_AccionRealizada', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('m_Observaciones', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('m_Personal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('m_HoraInicio', self.gf('django.db.models.fields.TimeField')()),
            ('m_HoraFin', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'eventos', ['Bitacora_Mantenimiento'])


    def backwards(self, orm):
        # Deleting model 'Mes'
        db.delete_table(u'eventos_mes')

        # Deleting model 'Mantenimiento_Categoria'
        db.delete_table(u'eventos_mantenimiento_categoria')

        # Deleting model 'Denominacion'
        db.delete_table(u'eventos_denominacion')

        # Deleting model 'Equipo'
        db.delete_table(u'eventos_equipo')

        # Deleting model 'Prioridad'
        db.delete_table(u'eventos_prioridad')

        # Deleting model 'CodigoCausa'
        db.delete_table(u'eventos_codigocausa')

        # Deleting model 'CodigoColor'
        db.delete_table(u'eventos_codigocolor')

        # Deleting model 'CategoriaMaterial'
        db.delete_table(u'eventos_categoriamaterial')

        # Deleting model 'Material'
        db.delete_table(u'eventos_material')

        # Deleting model 'ParteDeRepuesto'
        db.delete_table(u'eventos_partederepuesto')

        # Deleting model 'MaterialOcupado'
        db.delete_table(u'eventos_materialocupado')

        # Deleting model 'ParteDeRepuestoOcupada'
        db.delete_table(u'eventos_partederepuestoocupada')

        # Deleting model 'Evento_Mantenimiento'
        db.delete_table(u'eventos_evento_mantenimiento')

        # Deleting model 'Mantenimiento_Programado'
        db.delete_table(u'eventos_mantenimiento_programado')

        # Deleting model 'Tipo_Trabajo'
        db.delete_table(u'eventos_tipo_trabajo')

        # Deleting model 'Tipo_Mantenimiento'
        db.delete_table(u'eventos_tipo_mantenimiento')

        # Deleting model 'Orden_Mantenimiento'
        db.delete_table(u'eventos_orden_mantenimiento')

        # Removing M2M table for field m_PartesDeRepuestoOcupadas on 'Orden_Mantenimiento'
        db.delete_table(db.shorten_name(u'eventos_orden_mantenimiento_m_PartesDeRepuestoOcupadas'))

        # Removing M2M table for field m_MaterialesOcupados on 'Orden_Mantenimiento'
        db.delete_table(db.shorten_name(u'eventos_orden_mantenimiento_m_MaterialesOcupados'))

        # Removing M2M table for field m_CodigosdeCausa on 'Orden_Mantenimiento'
        db.delete_table(db.shorten_name(u'eventos_orden_mantenimiento_m_CodigosdeCausa'))

        # Removing M2M table for field m_Personal on 'Orden_Mantenimiento'
        db.delete_table(db.shorten_name(u'eventos_orden_mantenimiento_m_Personal'))

        # Deleting model 'Mantenimiento_Verificado'
        db.delete_table(u'eventos_mantenimiento_verificado')

        # Deleting model 'Mantenimiento_Validado'
        db.delete_table(u'eventos_mantenimiento_validado')

        # Deleting model 'Bitacora_Mantenimiento'
        db.delete_table(u'eventos_bitacora_mantenimiento')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'eventos.bitacora_mantenimiento': {
            'Meta': {'object_name': 'Bitacora_Mantenimiento'},
            'm_AccionRealizada': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'm_FechaHora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'm_HoraFin': ('django.db.models.fields.TimeField', [], {}),
            'm_HoraInicio': ('django.db.models.fields.TimeField', [], {}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Observaciones': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'm_OrdenMantenimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Orden_Mantenimiento']"}),
            'm_Personal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'm_ProblemaParo': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'eventos.categoriamaterial': {
            'Meta': {'object_name': 'CategoriaMaterial'},
            'm_CodigoColor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.CodigoColor']", 'max_length': '250'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_NombreCategoria': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'eventos.codigocausa': {
            'Meta': {'object_name': 'CodigoCausa'},
            'm_Causa': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'eventos.codigocolor': {
            'Meta': {'object_name': 'CodigoColor'},
            'm_ActividadRelacionada': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_Color': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'eventos.denominacion': {
            'Meta': {'object_name': 'Denominacion'},
            'm_Denominacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'eventos.equipo': {
            'Meta': {'object_name': 'Equipo'},
            'm_Fabricante': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Modelo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'eventos.evento_mantenimiento': {
            'Meta': {'object_name': 'Evento_Mantenimiento'},
            'm_AnyoIinicio': ('django.db.models.fields.IntegerField', [], {}),
            'm_Categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Mantenimiento_Categoria']"}),
            'm_Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'm_Frecuencia_meses': ('django.db.models.fields.IntegerField', [], {}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_MesInicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Mes']"}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'eventos.mantenimiento_categoria': {
            'Meta': {'object_name': 'Mantenimiento_Categoria'},
            'm_Abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'm_Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'eventos.mantenimiento_programado': {
            'Meta': {'object_name': 'Mantenimiento_Programado'},
            'm_Anyo': ('django.db.models.fields.IntegerField', [], {}),
            'm_EventoMantenimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Evento_Mantenimiento']"}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Mes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Mes']"})
        },
        u'eventos.mantenimiento_validado': {
            'Meta': {'object_name': 'Mantenimiento_Validado'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_MantenimientoProgramado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Mantenimiento_Programado']"}),
            'm_Validado': ('django.db.models.fields.BooleanField', [], {}),
            'm_ValidadoPor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'eventos.mantenimiento_verificado': {
            'Meta': {'object_name': 'Mantenimiento_Verificado'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_MantenimientoProgramado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Mantenimiento_Programado']"}),
            'm_Verificado': ('django.db.models.fields.BooleanField', [], {}),
            'm_VerificadoPor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'eventos.material': {
            'Meta': {'object_name': 'Material'},
            'm_Articulo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'm_CategoriaMaterial': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Denominacion'", 'to': u"orm['eventos.CategoriaMaterial']"}),
            'm_Denominacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Denominacion']"}),
            'm_Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'm_FechaCompra': ('django.db.models.fields.DateField', [], {}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_PrecioCompra': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'm_Proveedor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'm_Stock': ('django.db.models.fields.IntegerField', [], {})
        },
        u'eventos.materialocupado': {
            'Meta': {'object_name': 'MaterialOcupado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_CantidadAOcupar': ('django.db.models.fields.FloatField', [], {}),
            'm_Denominacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Denominacion'", 'to': u"orm['eventos.Denominacion']"}),
            'm_Material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Material'", 'to': u"orm['eventos.Material']"})
        },
        u'eventos.mes': {
            'Meta': {'object_name': 'Mes'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'eventos.orden_mantenimiento': {
            'Meta': {'object_name': 'Orden_Mantenimiento'},
            'm_CodigosdeCausa': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Codigos_Causas'", 'blank': 'True', 'to': u"orm['eventos.CodigoCausa']"}),
            'm_CostoTotal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'm_Equipo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Equipo'", 'null': 'True', 'to': u"orm['eventos.Equipo']"}),
            'm_FechaHoraCompletado': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'm_FechaHoraCreacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'm_FechaHoraMantAnt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_MaterialesOcupados': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Materiales_Ocupados'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['eventos.MaterialOcupado']"}),
            'm_PartesDeRepuestoOcupadas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Piezas_Repuesto_Ocupadas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['eventos.ParteDeRepuestoOcupada']"}),
            'm_Personal': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Personal'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'm_Prioridad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Prioridad'", 'to': u"orm['eventos.Prioridad']"}),
            'm_Programable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'm_Supervisor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Supervisor'", 'to': u"orm['auth.User']"}),
            'm_TipoMantenimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Tipo_Mantenimiento'", 'to': u"orm['eventos.Tipo_Mantenimiento']"}),
            'm_TipoTrabajo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Tipo_Trabajo'", 'to': u"orm['eventos.Tipo_Trabajo']"})
        },
        u'eventos.partederepuesto': {
            'Meta': {'object_name': 'ParteDeRepuesto'},
            'm_Articulo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_Equipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'EquipoMantenimiento'", 'to': u"orm['eventos.Equipo']"}),
            'm_FechaCompra': ('django.db.models.fields.DateField', [], {}),
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Marca': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_Modelo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'm_PrecioUnitario': ('django.db.models.fields.FloatField', [], {}),
            'm_Proveedor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'm_TotalEnStock': ('django.db.models.fields.FloatField', [], {})
        },
        u'eventos.partederepuestoocupada': {
            'Meta': {'object_name': 'ParteDeRepuestoOcupada'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_CantidadAOcupar': ('django.db.models.fields.FloatField', [], {}),
            'm_Denominacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Denominacion_Parte'", 'to': u"orm['eventos.Denominacion']"}),
            'm_Parte': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Parte_Repuesto'", 'to': u"orm['eventos.ParteDeRepuesto']"})
        },
        u'eventos.prioridad': {
            'Meta': {'object_name': 'Prioridad'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'eventos.tipo_mantenimiento': {
            'Meta': {'object_name': 'Tipo_Mantenimiento'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'eventos.tipo_trabajo': {
            'Meta': {'object_name': 'Tipo_Trabajo'},
            'm_ID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['eventos']