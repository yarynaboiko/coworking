from django.urls import path
from booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('book-room/<int:room_id>', views.book_room, name='book-room'),
]