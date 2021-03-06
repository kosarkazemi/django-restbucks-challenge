# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-20 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerEmail', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('WA', 'waiting'), ('PR', 'preparation'), ('RD', 'ready'), ('DV', 'delivered')], default='WA', max_length=2)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('option1', models.CharField(max_length=40)),
                ('option2', models.CharField(max_length=40)),
                ('option3', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django-restbucks-challenge.manager.Product'),
        ),
    ]
