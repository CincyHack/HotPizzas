# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20140922_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('view_product', 'view product'),)},
        ),
    ]
