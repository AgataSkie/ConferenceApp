# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConferenceApp', '0004_auto_20170112_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='fb',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
