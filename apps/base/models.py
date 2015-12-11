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


class News(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=35)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='news photos')
    corpus = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author