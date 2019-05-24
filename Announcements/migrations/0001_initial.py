# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Log_In', '__first__'),
        ('Courses', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=100)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Announcements', to='Courses.Courses')),
                ('Lect_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log_In.Lecturer')),
            ],
        ),
    ]