from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ]

    LANGUAGE_EN = "EN"
    LANGUAGE_KR = "KR"
    LANGUAGE_CHOICES = [
        (LANGUAGE_EN, "English"),
        (LANGUAGE_KR, "Korean"),
    ]

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"
    CURRENCY_CHOICES = [(CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW")]

    REQUIRED_FIELDS = []
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=GENDER_MALE,
        max_length=10,
        null=True,
        blank=True,
    )
    bio = models.TextField(default="", blank=True)

    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_KR
    )

    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_KRW
    )

    superhost = models.BooleanField(default=False)
