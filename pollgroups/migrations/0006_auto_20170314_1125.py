# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollgroups', '0005_auto_20170314_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursesession',
            options={'permissions': (('make_poll', 'Make Poll'),)},
        ),
    ]
