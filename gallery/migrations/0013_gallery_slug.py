# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20170804_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='Identificador'),
            preserve_default=False,
        ),
    ]
