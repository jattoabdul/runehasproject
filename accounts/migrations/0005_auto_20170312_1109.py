# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-12 10:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170312_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='course',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='matric_no',
        ),
        migrations.AddField(
            model_name='myprofile',
            name='department',
            field=models.CharField(max_length=250, null=True, verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Student Email'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='faculty',
            field=models.CharField(max_length=250, null=True, verbose_name='Faculty'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='homeAddress',
            field=models.TextField(blank=True, max_length=250, verbose_name='Permanent Home Address'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='level',
            field=models.IntegerField(null=True, verbose_name='Level(Year of Study)'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='mat_no',
            field=models.CharField(max_length=250, null=True, verbose_name="Student's Matric No"),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='mobileNo',
            field=models.PositiveIntegerField(null=True, verbose_name='Student Phone No'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='title',
            field=models.CharField(blank=True, choices=[('mr', 'Mr'), ('mi', 'Miss'), ('ms', 'Mrs')], max_length=2, verbose_name='Title(Mr/Miss/Mrs)'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='gender',
            field=models.CharField(choices=[('ML', 'MALE'), ('FL', 'FEMALE')], max_length=2, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='Student/Admin User'),
        ),
    ]