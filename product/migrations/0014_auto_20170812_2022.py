# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_dayline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayline',
            name='product',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
