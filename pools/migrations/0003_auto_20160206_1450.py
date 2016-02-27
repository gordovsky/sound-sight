# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_remove_point_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]
