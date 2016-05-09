# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20160509_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Author'),
        ),
    ]
