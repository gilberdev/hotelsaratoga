# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='url',
            field=models.TextField(default='#'),
            preserve_default=False,
        ),
    ]
