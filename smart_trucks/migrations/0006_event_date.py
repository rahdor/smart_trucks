# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0005_auto_20150203_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
    ]
