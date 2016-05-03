# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
