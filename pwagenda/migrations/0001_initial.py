# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('emails', models.EmailField(help_text='Type emails of participants', max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(default=datetime.datetime(2015, 5, 14, 5, 45, 13, 493097, tzinfo=utc), blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('item', models.CharField(max_length=250)),
                ('subitem1', models.CharField(max_length=250)),
                ('subitem2', models.CharField(max_length=250)),
                ('subitem3', models.CharField(max_length=250)),
                ('item1', models.CharField(max_length=250)),
                ('subitem4', models.CharField(max_length=250)),
                ('subitem5', models.CharField(max_length=250)),
                ('subitem6', models.CharField(max_length=250)),
                ('item2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=158, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
