# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-20 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fights', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sherdog_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
