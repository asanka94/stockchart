# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-01 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
    ]
