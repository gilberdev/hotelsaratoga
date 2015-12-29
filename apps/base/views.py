"""Views for the base app"""

from django.shortcuts import render
from .models import Hotel, Polaroid, New, Facility, General_Facility, SightSeen


def home(request):
    """ Default view for the root """
    polaroid_list = Polaroid.objects.all()

    (left_new, right_new) = New.objects.order_by('date')[:2]

    facilities_list = Facility.objects.all()
    facility_count = range(0, len(facilities_list))

    general_facility_lst = General_Facility.objects.all()
    sightseen_lst = SightSeen.objects.all()

    return render(request, 'base/home.html', {'polaroids': polaroid_list,
                                              'left_new': left_new,
                                              'right_new': right_new,
                                              'facilities_list': facilities_list,
                                              'facility_count': facility_count,
                                              'general_facility_lst': general_facility_lst,
                                              'sightseen_lst': sightseen_lst})

def history(request):
    """ Default view for the history """
    return render(request, 'base/history.html')

def news(request):
    """ Default view for the news """

    news_lst = New.objects.order_by('date').all()
    return render(request, 'base/news.html', {'news': news_lst})

def hotels(request):
    """ Default view for the hotels """
    hotel_list = Hotel.objects.all()

    return render(request, 'base/hotels.html', {'hotels': hotel_list})


