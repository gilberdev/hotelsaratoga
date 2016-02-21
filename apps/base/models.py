"""Base models"""
from django.db import models
from PIL import Image
import copy


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='hotel photos')
    stars = models.IntegerField()
    url = models.TextField()

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=35)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='news photos', null=True)
    corpus = models.TextField()

    def first_paragraph(self):
        t = self.corpus.partition('    ')
        return t[0]

    def rest(self):
        t = self.corpus.partition('    ')
        return t[2]

    def customize_date(self):
        a = self.date.strftime('%B %d, %Y, %H:%M%p')
        return a

    def __str__(self):
        return self.title + " by " + self.author


class Polaroid(models.Model):
    caption = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='polaroid photos')
    short_photo = models.ImageField(upload_to='polaroid short photos', default=None, null=True, blank=True)
    dummy = models.BooleanField(default=False)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        if not self.id and not self.photo:
            return

        super(Polaroid, self).save(*args, **kwargs)

        image = Image.open(self.short_photo)
        size = (240, 240)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.short_photo.path)


class Facility(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities_images')

    def __str__(self):
        return self.name


class General_Facility(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SightSeen(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_name = models.CharField(max_length=30,unique=True)
    room_description = models.TextField()
    room_bottom_message = models.TextField()
    room_picture = models.ImageField(upload_to="room_posters")

    def __str__(self):
        return self.room_name


class RoomPicture(models.Model):
    room = models.ForeignKey(Room)
    picture = models.ImageField(upload_to="rooms_gallery")
    picture_description = models.TextField()

    # def save(self):
    #
    #     if not self.id and not self.photo:
    #         return
    #
    #     super(Polaroid, self).save()
    #
    #     image = Image.open(self.photo)
    #     #(width, height) = image.size
    #
    #     #if (240 / width < 240 < height):
    #     #    factor = 240.0 / height
    #     #else:
    #     #    factor = 240.0 / width
    #
    #     size = (240, 240)
    #     image = image.resize(size, Image.ANTIALIAS)
    #     image.save(self.photo.path)


class History(models.Model):
    history_text = models.TextField()
