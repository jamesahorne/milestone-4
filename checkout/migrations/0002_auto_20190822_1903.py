# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-22 19:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
