"""Views for the base app"""

from django.shortcuts import render
from .models import Hotel, Polaroid, New


def home(request):
    """ Default view for the root """
    polaroid_list = Polaroid.objects.all()

    (left_new, right_new) = New.objects.order_by('date')[:2]

    return render(request, 'base/home.html', {'polaroids': polaroid_list, 'left_new': left_new, 'right_new': right_new})

def history(request):
    """ Default view for the history """
    return render(request, 'base/history.html')

def news(request):
    """ Default view for the news """
    return render(request, 'base/news.html')

def hotels(request):
    """ Default view for the hotels """
    hotel_list = Hotel.objects.all()

    return render(request, 'base/hotels.html', {'hotels': hotel_list})


