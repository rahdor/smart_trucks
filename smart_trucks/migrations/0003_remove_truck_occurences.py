# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0002_auto_20150124_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='occurences',
        ),
    ]
