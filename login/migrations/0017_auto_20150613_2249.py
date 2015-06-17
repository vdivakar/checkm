# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_answered_who'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='answered',
            new_name='answer',
        ),
    ]
