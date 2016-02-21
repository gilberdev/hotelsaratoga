# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_hotel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
