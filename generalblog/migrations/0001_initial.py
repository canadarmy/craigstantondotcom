# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-22 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(choices=[('GENERAL_PYTHON', 'General Python'), ('DJANGO', 'Django'), ('BLOCKCHAIN', 'Blockchain'), ('DATA_SCIENCE', 'Data Science'), ('ARTIFICIAL_INTELLIGENCE', 'AI'), ('RANDOM_THOUGHTS', 'Random Thoughts')], default='RANDOM_THOUGHTS', max_length=255)),
                ('post_name', models.CharField(max_length=255)),
                ('post_description', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True, max_length=255)),
                ('updated_date', models.DateTimeField(auto_now_add=True, max_length=255)),
                ('post_content', models.FileField(default=None, max_length=255, upload_to='static/blogfiles')),
            ],
        ),
    ]
