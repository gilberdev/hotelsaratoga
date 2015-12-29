"""Base models"""
from django.db import models
from PIL import Image


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='hotel photos')
    stars = models.IntegerField()

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=35)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='news photos', null=True)
    corpus = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author


class Polaroid(models.Model):
    caption = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='polaroid photos')
    dummy = models.BooleanField(default=False)

    def __str__(self):
        return self.caption

    def save(self):

        if not self.id and not self.photo:
            return

        super(Polaroid, self).save()

        image = Image.open(self.photo)
        #(width, height) = image.size

        #if (240 / width < 240 < height):
        #    factor = 240.0 / height
        #else:
        #    factor = 240.0 / width

        size = (240, 240)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)


class Facility(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities_images')

    def __str__(self):
        return self.name

class General_Facility(models.Model):
    name = models.CharField(max_length=30)

class SightSeen(models.Model):
    name = models.CharField(max_length=30)