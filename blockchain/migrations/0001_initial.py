# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-22 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BCChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('selection', models.CharField(choices=[('COIN', 'Buy Coins'), ('CONTRACT', 'Contract Craig'), ('TEST', 'Test Blockchain'), ('RESEARCH', 'Research')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cryptocurrencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('name_id', models.CharField(blank=True, max_length=100)),
                ('symbol', models.CharField(blank=True, max_length=100)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('price_usd', models.FloatField(null=True)),
                ('price_btc', models.FloatField(null=True)),
                ('volume_24h_usd', models.FloatField(null=True)),
                ('market_cap_usd', models.FloatField(null=True)),
                ('available_supply', models.FloatField(null=True)),
                ('total_supply', models.FloatField(null=True)),
                ('max_supply', models.FloatField(null=True)),
                ('percent_change_1h', models.FloatField(null=True)),
                ('percent_change_24h', models.FloatField(null=True)),
                ('percent_change_7d', models.FloatField(null=True)),
                ('last_updated', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bcchoice',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blockchain.Blockchain'),
        ),
    ]
