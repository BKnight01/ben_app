# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-25 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticket_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('Severe', 'Severe'), ('Moderate', 'Moderate'), ('Minor', 'Minor')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Under Review', 'Under Review'), ('Solved', 'Solved')], default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
