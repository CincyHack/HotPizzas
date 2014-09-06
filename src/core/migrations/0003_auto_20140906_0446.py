# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140906_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotpizzasuser',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='hotpizzasuser',
            name='last_location',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotpizzasuser',
            name='latitude',
            field=models.DecimalField(decimal_places=5, null=True, max_digits=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotpizzasuser',
            name='longitude',
            field=models.DecimalField(decimal_places=5, null=True, max_digits=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='delivered_latitude',
            field=models.DecimalField(decimal_places=5, blank=True, null=True, max_digits=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='delivered_longitude',
            field=models.DecimalField(decimal_places=5, blank=True, null=True, max_digits=10),
            preserve_default=True,
        ),
    ]
