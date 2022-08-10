from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    def handle(self, *args, **options):
        facilities = [
            "Pool",
            "Hot tub",
            "Free parking on premises",
            "EV charger",
            "Crib",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]

        for facility in facilities:
            Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created!"))
