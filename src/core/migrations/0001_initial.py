# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('core_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
        ))
        db.send_create_signal('core', ['Location'])

        # Adding model 'Customer'
        db.create_table('core_customer', (
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=15)),
        ))
        db.send_create_signal('core', ['Customer'])

        # Adding model 'CustomerInformation'
        db.create_table('core_customerinformation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='customer_informations', to=orm['core.Customer'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='customer', to=orm['core.Location'])),
        ))
        db.send_create_signal('core', ['CustomerInformation'])

        # Adding model 'Driver'
        db.create_table('core_driver', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Driver'])

        # Adding model 'ProductType'
        db.create_table('core_producttype', (
            ('name', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=20)),
        ))
        db.send_create_signal('core', ['ProductType'])

        # Adding model 'ProductConfiguration'
        db.create_table('core_productconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductType'])),
        ))
        db.send_create_signal('core', ['ProductConfiguration'])

        # Adding model 'Product'
        db.create_table('core_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cook_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiration_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('base_price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductType'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['core.CustomerInformation'], blank=True, null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['core.Location'])),
            ('driver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['core.Driver'])),
            ('delivered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
        ))
        db.send_create_signal('core', ['Product'])

        # Adding M2M table for field configurations on 'Product'
        m2m_table_name = db.shorten_name('core_product_configurations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['core.product'], null=False)),
            ('productconfiguration', models.ForeignKey(orm['core.productconfiguration'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'productconfiguration_id'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('core_location')

        # Deleting model 'Customer'
        db.delete_table('core_customer')

        # Deleting model 'CustomerInformation'
        db.delete_table('core_customerinformation')

        # Deleting model 'Driver'
        db.delete_table('core_driver')

        # Deleting model 'ProductType'
        db.delete_table('core_producttype')

        # Deleting model 'ProductConfiguration'
        db.delete_table('core_productconfiguration')

        # Deleting model 'Product'
        db.delete_table('core_product')

        # Removing M2M table for field configurations on 'Product'
        db.delete_table(db.shorten_name('core_product_configurations'))


    models = {
        'core.customer': {
            'Meta': {'object_name': 'Customer'},
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '15'})
        },
        'core.customerinformation': {
            'Meta': {'object_name': 'CustomerInformation'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer_informations'", 'to': "orm['core.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer'", 'to': "orm['core.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.driver': {
            'Meta': {'object_name': 'Driver'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'base_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'configurations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.ProductConfiguration']"}),
            'cook_time': ('django.db.models.fields.DateTimeField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['core.CustomerInformation']", 'blank': 'True', 'null': 'True'}),
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['core.Driver']"}),
            'expiration_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['core.Location']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['core']