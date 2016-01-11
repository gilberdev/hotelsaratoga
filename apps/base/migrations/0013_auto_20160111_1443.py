# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_room_roompicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_bottom_message',
            field=models.TextField(),
        ),
    ]
