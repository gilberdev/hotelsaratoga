# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20151220_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='polaroid',
            name='dummy',
            field=models.BooleanField(default=False),
        ),
    ]
