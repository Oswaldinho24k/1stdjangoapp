# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('likes', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publicado', models.BooleanField(default=False)),
            ],
        ),
    ]
