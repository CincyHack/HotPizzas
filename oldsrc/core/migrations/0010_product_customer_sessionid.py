# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20140930_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer_sessionid',
            field=models.CharField(null=True, blank=True, max_length=32),
            preserve_default=True,
        ),
    ]
