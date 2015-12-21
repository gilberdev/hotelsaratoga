__author__ = 'Gilber'
from django.contrib import admin

from .models import Hotel, New, Polaroid

admin.site.register(Hotel)
admin.site.register(New)
admin.site.register(Polaroid)
