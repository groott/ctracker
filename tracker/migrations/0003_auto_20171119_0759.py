# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 06:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_client_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('unit_type', models.CharField(choices=[('cpc', 'CPC'), ('cpm', 'CPM'), ('cpv', 'CPV')], default='cpc', max_length=3)),
                ('units', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('budget_spent', models.IntegerField(default=0)),
                ('units_delivered', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='client_name',
        ),
        migrations.AddField(
            model_name='campaign',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Client'),
        ),
    ]
