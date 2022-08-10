import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        help = "This command create many rooms."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_amenities = room_models.Amenity.objects.all()
        all_facilities = room_models.Facility.objects.all()
        all_houserules = room_models.HouseRule.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "amenities": lambda x: random.choice(all_amenities),
                "facilities": lambda x: random.choice(all_facilities),
                "house_rules": lambda x: random.choice(all_houserules),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Room(s) created!"))
