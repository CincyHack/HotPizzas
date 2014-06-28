# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CustomerInformation'
        db.delete_table('core_customerinformation')

        # Adding field 'Customer.name'
        db.add_column('core_customer', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CustomerInformation'
        db.create_table('core_customerinformation', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['CustomerInformation'])

        # Deleting field 'Customer.name'
        db.delete_column('core_customer', 'name')


    models = {
        'core.customer': {
            'Meta': {'object_name': 'Customer'},
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'})
        },
        'core.driver': {
            'Meta': {'object_name': 'Driver'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'base_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'configurations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.ProductConfiguration']"}),
            'cook_time': ('django.db.models.fields.DateTimeField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['core.Customer']", 'null': 'True'}),
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Driver']"}),
            'expiration_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductType']"}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'core.productconfiguration': {
            'Meta': {'object_name': 'ProductConfiguration'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductType']"})
        },
        'core.producttype': {
            'Meta': {'object_name': 'ProductType'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']