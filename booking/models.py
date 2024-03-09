from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="назва")
    description = models.TextField(verbose_name="опис")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']

class Room(models.Model):
    title = models.CharField(max_length=50, verbose_name="назва кімнати")
    capacity = models.IntegerField(verbose_name="місткість кімнати")
    description = models.TextField(verbose_name="опис")
    image = models.ImageField(upload_to='rooms')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категорія кімнати")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ціна кімнати")
    location = models.CharField(max_length=255, verbose_name="локація кімнати")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'
        ordering = ['category']


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name="назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ціна")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="кімната")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Місце'
        verbose_name_plural = 'Місця'
        ordering = ['room']


class Booking(models.Model):
    BOOKING_STATUSES = [
        ("created", "Створене бронювання"),
        ("confirmed", "Підтверджене бронювання"),
        ("cancelled", "Скасовано бронювання"),
        ("archived", "Минуле бронювання"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="користувач")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="кімната")
    places = models.ManyToManyField(Place, related_name="bookings", verbose_name="місця")
    start_date = models.DateTimeField(verbose_name="дата початку")
    end_date = models.DateTimeField(verbose_name="кінцева дата")
    status = models.CharField(max_length=30, choices=BOOKING_STATUSES, default='created', verbose_name="статус")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="створена дата")
    def __str__(self):
        return f'{self.pk}, {self.room}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['created_date']
