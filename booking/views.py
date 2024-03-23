from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from booking.models import Category


# Create your views here.
def index(request):

    context = {
        'categories': Category.objects.all()
    }

    return render (request, 'booking/index.html', context=context)


@login_required(login_url='/login/')
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    context = {
        "category": category
    }
    return render(request, 'booking/category_page.html', context=context)