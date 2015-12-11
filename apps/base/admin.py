__author__ = 'Gilber'
from django.contrib import admin

from .models import Hotel, News

admin.site.register(Hotel)
admin.site.register(News)
