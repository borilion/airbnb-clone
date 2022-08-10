from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                ),
            },
        ),
        (
            "Times",
            {
                "classes": ("collapse",),
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                ),
            },
        ),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": (
                    "beds",
                    "bedrooms",
                    "baths",
                    "guests",
                ),
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "house_rules",
                    "facilities",
                ),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("host",),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "room_type",
        "count_amenities",
        "count_facilities",
        "count_house_rules",
        "count_photos",
        "total_rating",
    )

    raw_id_fields = ("host",)

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenities",
        "house_rules",
        "facilities",
        "country",
    )

    search_fields = ["city", "^host__username"]
    filter_horizontal = (
        "amenities",
        "house_rules",
        "facilities",
    )

    def count_amenities(self, room_object):
        return room_object.amenities.count()

    count_amenities.short_description = "Amenities"

    def count_facilities(self, room_object):
        return room_object.facilities.count()

    count_facilities.short_description = "Facilities"

    def count_house_rules(self, room_object):
        return room_object.house_rules.count()

    count_house_rules.short_description = "House Rules"

    def count_photos(self, room_object):
        return room_object.photos.count()

    count_photos.short_description = "Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="50px" />')

    get_thumbnail.short_description = "Thumbnail"
