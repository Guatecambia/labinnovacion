# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoproyecto', '0002_auto_20180207_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipality',
            name='long',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipality',
            name='zoom',
            field=models.PositiveSmallIntegerField(default=12),
            preserve_default=False,
        ),
    ]
