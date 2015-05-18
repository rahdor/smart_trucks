# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='trucks',
            field=models.ManyToManyField(to='smart_trucks.Truck'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='truck',
            name='occurences',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
