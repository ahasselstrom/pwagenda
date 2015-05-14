# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pwagenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 45, 19, 569175, tzinfo=utc), blank=True),
        ),
    ]
