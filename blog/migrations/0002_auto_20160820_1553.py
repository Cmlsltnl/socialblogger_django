# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_field',
            field=models.FileField(blank=True, null=True, upload_to='profile/%Y/%m/%d'),
        ),
    ]
