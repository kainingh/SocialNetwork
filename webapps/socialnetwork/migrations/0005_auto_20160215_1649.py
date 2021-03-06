# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0004_auto_20160215_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.FileField(blank=True, upload_to='person-photo'),
        ),
    ]
