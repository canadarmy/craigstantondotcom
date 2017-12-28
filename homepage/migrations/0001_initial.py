# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('selection', models.CharField(choices=[('COIN', 'Buy Coins'), ('CONTRACT', 'Contract Craig'), ('TEST', 'Test Blockchain')], max_length=1)),
            ],
        ),
    ]
