# Generated by Django 2.1.2 on 2018-10-24 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_event_registration_close_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='registration_close_time',
            new_name='hours_before_registration_close_time',
        ),
    ]