# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
