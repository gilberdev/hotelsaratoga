"""Views for the base app"""

from django.shortcuts import render
from .models import Hotel


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

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


