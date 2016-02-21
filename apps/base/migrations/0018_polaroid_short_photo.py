# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20160219_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='polaroid',
            name='short_photo',
            field=models.ImageField(null=True, upload_to=b'polaroid short photos', blank=True),
        ),
    ]
