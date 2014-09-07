# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20140906_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotpizzasuser',
            name='latitude',
            field=models.DecimalField(blank=True, null=True, decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='hotpizzasuser',
            name='longitude',
            field=models.DecimalField(blank=True, null=True, decimal_places=5, max_digits=10),
        ),
    ]
