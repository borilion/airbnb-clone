# Generated by Django 4.1rc1 on 2022-07-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="superhost",
            field=models.BooleanField(default=False),
        ),
    ]
