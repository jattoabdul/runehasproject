# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-30 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runehas', '0004_auto_20170312_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bname',
            field=models.CharField(choices=[('BA', 'Bed A'), ('BB', 'Bed B')], max_length=2, null=True, verbose_name='Bed Name'),
        ),
    ]
