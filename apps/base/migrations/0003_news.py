# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151210_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=35)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to=b'news photos')),
                ('corpus', models.TextField()),
            ],
        ),
    ]
