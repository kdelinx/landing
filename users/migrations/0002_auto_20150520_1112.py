# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 11, 12, 32, 382416, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
