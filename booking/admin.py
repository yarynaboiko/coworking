from django.contrib import admin

from booking.models import Category, Room, Place, Booking

# Register your models here.
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Place)
admin.site.register(Booking)