# Generated by Django 4.1 on 2022-08-11 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_alter_review_room_alter_review_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="localtion",
            new_name="location",
        ),
    ]
