from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from booking.models import Category, Room


# Create your views here.
def index(request):

    context = {
        'categories': Category.objects.all()
    }

    return render (request, 'booking/index.html', context=context)


@login_required(login_url='/login/')
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    rooms = Room.objects.filter(category=category)

    start_datetime =  request.GET.get("start_datetime")
    end_datetime =  request.GET.get("end_datetime")

    if start_datetime and end_datetime:
        rooms = rooms.exclude(bookings__start_date__lt = end_datetime, bookings__end_date__gt = start_datetime)

    context = {
        "category": category,
        "rooms": rooms,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }
    return render(request, 'booking/category_page.html', context=context)


class Bookings:
    pass


@login_required(login_url='/login/')
def book_room(request, room_id):
    start_datetime = request.GET.get("start_datetime")
    end_datetime = request.GET.get("end_datetime")

    room = get_object_or_404(Room, id=room_id)
    if start_datetime and end_datetime:
        new_booking = Bookings.objects.create(
            user = request.user,
            room = room,
            start_date = start_datetime,
            end_date = end_datetime
        )

        return HttpResponse("Бронювання оформлено")
    return HttpResponse("Помилка")
