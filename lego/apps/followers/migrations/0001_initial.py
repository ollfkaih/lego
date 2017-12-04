# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 10:20
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20170828_1020'),
        ('companies', '0002_auto_20170828_1020'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowCompany',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                (
                    'follower',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'target',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='followers',
                        to='companies.Company'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='FollowEvent',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                (
                    'follower',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'target',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='followers',
                        to='events.Event'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    )
                ),
                (
                    'updated_at',
                    models.DateTimeField(default=django.utils.timezone.now, editable=False)
                ),
                ('deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                (
                    'follower',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'target',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='followers',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='followuser',
            unique_together=set([('follower', 'target')]),
        ),
        migrations.AlterUniqueTogether(
            name='followevent',
            unique_together=set([('follower', 'target')]),
        ),
        migrations.AlterUniqueTogether(
            name='followcompany',
            unique_together=set([('follower', 'target')]),
        ),
    ]
