# Generated by Django 4.1rc1 on 2022-07-25 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_facility_remove_room_room_type_room_facilities_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"ordering": ["name"], "verbose_name_plural": "Amenities"},
        ),
        migrations.AlterModelOptions(
            name="facility",
            options={"ordering": ["name"], "verbose_name_plural": "Facilities"},
        ),
        migrations.AlterModelOptions(
            name="houserule",
            options={"ordering": ["name"], "verbose_name": "House Rule"},
        ),
        migrations.AlterModelOptions(
            name="roomtype",
            options={"ordering": ["name"], "verbose_name": "Room Type"},
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("caption", models.CharField(max_length=80)),
                ("file", models.ImageField(upload_to="")),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]