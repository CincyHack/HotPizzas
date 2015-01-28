# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20140906_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliverable_range',
            field=models.IntegerField(blank=True, null=True, default=10),
            preserve_default=True,
        ),
    ]
