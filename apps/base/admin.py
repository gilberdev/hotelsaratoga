__author__ = 'Gilber'
from django.contrib import admin

from .models import Hotel, New, Polaroid, Facility, General_Facility, SightSeen, Room, RoomPicture, History

admin.site.register(Hotel)
admin.site.register(New)
admin.site.register(Polaroid)
admin.site.register(Facility)
admin.site.register(General_Facility)
admin.site.register(SightSeen)
admin.site.register(Room)
admin.site.register(RoomPicture)
admin.site.register(History)



