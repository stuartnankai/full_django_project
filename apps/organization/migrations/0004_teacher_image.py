# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-15 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180509_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'teacher/%Y/%m', verbose_name=b'figure'),
        ),
    ]
