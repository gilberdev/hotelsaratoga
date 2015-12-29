# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_general_facility_sightseen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_facility',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sightseen',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
