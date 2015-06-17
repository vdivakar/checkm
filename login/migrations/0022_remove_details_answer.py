# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20150613_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='answer',
        ),
    ]
