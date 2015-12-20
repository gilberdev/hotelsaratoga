__author__ = 'Gilber'
from django.contrib import admin

from .models import Hotel, News, Polaroid

admin.site.register(Hotel)
admin.site.register(News)
admin.site.register(Polaroid)
