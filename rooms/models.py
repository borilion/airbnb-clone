from django.db import models
from core import models as core_models
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """Room Type Object Definition"""

    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """Amenity Object Definition"""

    pass

    class Meta:
        verbose_name_plural = "Amenities"
        ordering = ["name"]


class HouseRule(AbstractItem):

    """House Rule Object Definition"""

    pass

    class Meta:
        verbose_name = "House Rule"
        ordering = ["name"]


class Facility(AbstractItem):

    """Facility Object Definition"""

    pass

    class Meta:
        verbose_name_plural = "Facilities"
        ordering = ["name"]


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140, null=True)
    description = models.TextField(default="")
    country = CountryField(default="KR")
    city = models.CharField(max_length=80, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=140, default="")
    beds = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    baths = models.IntegerField(default=1)
    guests = models.IntegerField(default=0)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, null=True
    )
    room_type = models.ForeignKey(
        "RoomType",
        related_name="rooms",
        on_delete=models.SET_NULL,
        null=True,
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)  # Call the real save() method

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()

        if len(all_reviews) == 0:
            return 0
        else:
            return round(all_ratings / len(all_reviews), 2)
