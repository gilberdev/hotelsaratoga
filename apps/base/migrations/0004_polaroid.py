# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polaroid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to=b'polaroid photos')),
            ],
        ),
    ]
