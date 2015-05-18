# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0006_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
