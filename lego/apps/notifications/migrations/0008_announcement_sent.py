# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-14 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20170714_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='sent',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]