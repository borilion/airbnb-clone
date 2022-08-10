from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    """def add_arguments(self, parser):

        parser.add_argument(
            "-t",
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )"""

    def handle(self, *args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
        ]

        for amenity in amenities:
            Amenity.objects.create(name=amenity)

        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} Amenities Created!"))
