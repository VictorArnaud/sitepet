# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20170216_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='recent_picture',
            field=models.BooleanField(default=False, verbose_name='Imagem mais recente'),
        ),
    ]
