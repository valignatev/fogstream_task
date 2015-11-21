# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 18, 31, 52, 103205, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
