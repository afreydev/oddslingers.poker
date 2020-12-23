# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebets', '0003_auto_20180424_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebet',
            name='status',
            field=models.CharField(choices=[('opening', 'Opening'), ('active', 'Active'), ('closing', 'Closing'), ('closed', 'Closed')], default='active', max_length=25),
        ),
    ]