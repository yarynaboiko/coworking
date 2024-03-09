from django.shortcuts import render

from booking.models import Category


# Create your views here.
def index(request):

    context = {
        'categories': Category.objects.all()
    }

    return render (request, 'booking/index.html', context=context)

def category(request, category_id):
    return render(request, 'booking/category_page.html')