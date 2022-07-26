from django.db import models
from core import models as core_models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    communication = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    cleanliness = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    localtion = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    check_in = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    value = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.review} - {self.room}"
