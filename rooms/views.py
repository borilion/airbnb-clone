from datetime import datetime
from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page")
    # print(page or 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]

    # page_count = ceil(models.Room.objects.count() / page_size)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)

    return render(
        request,
        "rooms/home.html",
        context={"rooms": rooms},
    )
