# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_remove_gallery_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]