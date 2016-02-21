# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20160111_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('history_text', models.TextField()),
            ],
        ),
    ]
