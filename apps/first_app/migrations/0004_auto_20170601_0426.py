# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20170531_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
