# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-08 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[(b'pxjg', b'Traning Organization'), (b'school', b'School'), (b'Individual', b'Individual')], default=b'pxjg', max_length=20, verbose_name=b'orgname'),
        ),
    ]
