# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotPizzasUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=75)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_driver', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', blank=True, to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cook_time', models.DateTimeField()),
                ('expiration_time', models.DateTimeField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('delivered', models.BooleanField(default=False)),
                ('request_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productconfiguration',
            name='product_type',
            field=models.ForeignKey(to='core.ProductType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='configurations',
            field=models.ManyToManyField(to='core.ProductConfiguration'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(related_name='products-orders', blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='driver',
            field=models.ForeignKey(related_name='products-deliveries', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(related_name='products', to='core.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(to='core.ProductType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotpizzasuser',
            name='location',
            field=models.ForeignKey(related_name='user', to='core.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotpizzasuser',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_name='user_set', blank=True, to='auth.Permission', related_query_name='user', help_text='Specific permissions for this user.'),
            preserve_default=True,
        ),
    ]
