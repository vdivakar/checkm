# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0003_auto_20150603_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='user',
            field=models.ForeignKey(default=4, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
