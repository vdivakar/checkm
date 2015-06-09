# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0004_auto_20150601_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 3, 17, 44, 46, 25000, tzinfo=utc), to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]
