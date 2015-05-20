# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150520_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 11, 13, 11, 800187, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
