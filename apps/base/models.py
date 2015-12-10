"""Base models"""
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='hotel photos')
    stars = models.IntegerField()

    def __str__(self):
        return self.name