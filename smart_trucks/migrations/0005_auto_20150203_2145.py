# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0004_auto_20150131_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_location',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='facebook_id',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
