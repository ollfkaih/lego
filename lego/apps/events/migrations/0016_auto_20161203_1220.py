# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-03 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_merge_20161122_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price_guest',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='price_member',
            field=models.PositiveIntegerField(default=0),
        ),
    ]