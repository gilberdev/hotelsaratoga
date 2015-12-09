"""Views for the base app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def history(request):
    """ Default view for the root """
    return render(request, 'base/history.html')

def news(request):
    """ Default view for the root """
    return render(request, 'base/news.html')

def hotels(request):
    """ Default view for the root """
    return render(request, 'base/hotels.html')


