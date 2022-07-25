# Generated by Django 4.1rc1 on 2022-07-25 07:44

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_address_room_baths_room_bedrooms_room_beds_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="room",
            name="country",
            field=django_countries.fields.CountryField(default="KR", max_length=2),
        ),
        migrations.AddField(
            model_name="room",
            name="room_type",
            field=models.ManyToManyField(to="rooms.roomtype"),
        ),
    ]