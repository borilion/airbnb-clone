# Generated by Django 4.1rc1 on 2022-07-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0005_houserule"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(blank=True, to="rooms.houserule"),
        ),
    ]
