# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-25 12:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='comment')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'coursecomment',
                'verbose_name_plural': 'coursecomment',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='username')),
                ('mobile', models.CharField(max_length=12, verbose_name='phonenum')),
                ('course_name', models.CharField(max_length=50, verbose_name='coursename')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
            ],
            options={
                'verbose_name': 'userask',
                'verbose_name_plural': 'userask',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'usercourse',
                'verbose_name_plural': 'usercourse',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='dataid')),
                ('fav_type', models.IntegerField(choices=[('1', 'course'), ('2', 'org'), ('3', 'teacher')], default=1, verbose_name='fav_type')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'userfav',
                'verbose_name_plural': 'userfav',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='receiveuser')),
                ('message', models.CharField(max_length=500, verbose_name='message')),
                ('has_read', models.BooleanField(default=False, verbose_name='isread')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
            ],
            options={
                'verbose_name': 'usermessage',
                'verbose_name_plural': 'usermessage',
            },
        ),
    ]
