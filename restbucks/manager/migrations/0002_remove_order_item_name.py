# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-22 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='name',
        ),
    ]
