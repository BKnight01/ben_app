# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-25 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20180124_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]