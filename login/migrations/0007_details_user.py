# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0006_remove_details_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 3, 23, 25, 40, 466000), to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]
