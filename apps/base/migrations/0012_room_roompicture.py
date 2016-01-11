# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20151229_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=30)),
                ('room_description', models.TextField()),
                ('room_bottom_message', models.CharField(max_length=100)),
                ('room_picture', models.ImageField(upload_to=b'room_posters')),
            ],
        ),
        migrations.CreateModel(
            name='RoomPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'rooms_gallery')),
                ('picture_description', models.TextField()),
                ('room', models.ForeignKey(to='base.Room')),
            ],
        ),
    ]
