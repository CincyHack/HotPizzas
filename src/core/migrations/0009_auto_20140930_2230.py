# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20140929_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotpizzasuser',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.AddField(
            model_name='product',
            name='customer_latitude',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='customer_longitude',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='customer_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='customer_phone_number',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='purchased',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
