# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sidebets', '0004_auto_20180425_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebet',
            name='sidebet_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sidebets.Sidebet'),
        ),
    ]
