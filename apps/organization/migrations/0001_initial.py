# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-25 12:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='cityname')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=200, verbose_name='description')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'city',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='orgname')),
                ('desc', models.TextField(verbose_name='description')),
                ('click_num', models.IntegerField(default=0, verbose_name='clicknumber')),
                ('fav_num', models.IntegerField(default=0, verbose_name='savenum')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='figure')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='incity')),
            ],
            options={
                'verbose_name': 'courseorg',
                'verbose_name_plural': 'courseorg',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='teachername')),
                ('work_years', models.IntegerField(default=0, verbose_name='workyear')),
                ('work_company', models.CharField(max_length=50, verbose_name='companyrname')),
                ('work_position', models.CharField(max_length=50, verbose_name='position')),
                ('points', models.CharField(max_length=50, verbose_name='strenght')),
                ('click_num', models.IntegerField(default=0, verbose_name='clicknumber')),
                ('fav_num', models.IntegerField(default=0, verbose_name='savenum')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='inorg')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teacher',
            },
        ),
    ]