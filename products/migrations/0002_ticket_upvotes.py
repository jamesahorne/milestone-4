# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-12 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
