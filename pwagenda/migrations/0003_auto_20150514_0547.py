# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pwagenda', '0002_auto_20150514_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 47, 14, 266293, tzinfo=utc), blank=True),
        ),
    ]
