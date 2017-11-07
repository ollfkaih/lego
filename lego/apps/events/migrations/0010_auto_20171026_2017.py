# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:17
from __future__ import unicode_literals

from django.db import migrations

import lego.apps.content.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20171023_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='images',
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=lego.apps.content.fields.ContentField(allow_images=False, blank=True),
        ),
    ]