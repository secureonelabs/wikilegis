# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camara_deputados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinfo',
            name='reporting_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='camara_deputados.ReportingMember', verbose_name='Relator'),
        ),
    ]