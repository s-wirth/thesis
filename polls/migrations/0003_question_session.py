# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollgroups', '0001_initial'),
        ('polls', '0002_auto_20170308_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pollgroups.CourseSession'),
        ),
    ]
