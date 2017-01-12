# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('abstract', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=60)),
                ('bio', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceApp.Speaker'),
        ),
        migrations.AddField(
            model_name='session',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConferenceApp.Track'),
        ),
    ]