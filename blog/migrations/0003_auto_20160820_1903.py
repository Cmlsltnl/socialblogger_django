# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160820_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_field',
            field=models.FileField(blank=True, default=None, upload_to='profile/%Y/%m/%d'),
        ),
    ]
