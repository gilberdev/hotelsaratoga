# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_polaroid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polaroid',
            old_name='title',
            new_name='caption',
        ),
    ]
