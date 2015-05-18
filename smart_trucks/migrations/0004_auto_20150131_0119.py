# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trucks', '0003_remove_truck_occurences'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='truck_name',
            new_name='name',
        ),
    ]
