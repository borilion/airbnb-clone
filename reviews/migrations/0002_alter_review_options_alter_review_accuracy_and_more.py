# Generated by Django 4.1rc1 on 2022-07-26 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterField(
            model_name="review",
            name="accuracy",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="check_in",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="cleanliness",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="communication",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="localtion",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="value",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MaxValueValidator(5.0),
                    django.core.validators.MinValueValidator(0.1),
                ],
            ),
        ),
    ]
