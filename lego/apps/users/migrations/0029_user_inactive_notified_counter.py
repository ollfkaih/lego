# Generated by Django 2.2.19 on 2021-10-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0028_auto_20210523_1252"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="inactive_notified_counter",
            field=models.IntegerField(default=0),
        ),
    ]
