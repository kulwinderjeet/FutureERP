# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=20, unique=True)),
                ('wholesale_price', models.PositiveIntegerField(default=0)),
                ('retail_price', models.PositiveIntegerField(default=0)),
                ('img', models.ImageField(default='prod_imgs/default.png', upload_to='prod_imgs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
