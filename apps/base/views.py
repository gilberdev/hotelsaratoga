"""Views for the base app"""

from django.shortcuts import render
from .models import Hotel, Polaroid, New, Facility, General_Facility, SightSeen, Room, RoomPicture


def home(request):
    """ Default view for the root """
    polaroid_list = Polaroid.objects.all()

    (left_new, right_new) = New.objects.order_by('date')[:2]

    rooms_list = []
    rooms = Room.objects.all().order_by('room_name')

    for i in rooms:
        gallery = RoomPicture.objects.filter(room=i.id).all()
        rooms_list.append((i, gallery))

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
                                              'sightseen_lst': sightseen_lst,
                                              'rooms_list': rooms_list})

def history(request):
    """ Default view for the history """
    return render(request, 'base/history.html')

def news(request, new_id=""):
    """ Default view for the news """

    news_lst = New.objects.order_by('date').all()
    return render(request, 'base/news.html', {'news': news_lst,
                                              'id': new_id})

def hotels(request):
    """ Default view for the hotels """
    hotel_list = Hotel.objects.all()

    return render(request, 'base/hotels.html', {'hotels': hotel_list})


