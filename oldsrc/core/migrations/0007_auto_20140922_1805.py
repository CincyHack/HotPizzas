# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20140922_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotpizzasuser',
            options={'permissions': (('view_hotpizzasuser', 'view hot pizzas user'),)},
        ),
    ]
