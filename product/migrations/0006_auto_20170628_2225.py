# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170628_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceflow',
            name='note',
            field=models.CharField(max_length=255, null=True),
        ),
    ]