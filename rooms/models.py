from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models


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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
