# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20170812_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceflow',
            name='trade_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tradeflow',
            name='trade_time',
            field=models.DateTimeField(help_text='\u6210\u4ea4\u65f6\u95f4', null=True),
        ),
        migrations.AlterModelTable(
            name='priceflow',
            table='product_price_flow',
        ),
    ]
