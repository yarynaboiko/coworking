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
    title = models.CharField(max_length=50)
    capacity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='rooms')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'
        ordering = ['category']


class Place(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place, related_name="bookings")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=BOOKING_STATUSES, default='created')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}, {self.room}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['created_date']
