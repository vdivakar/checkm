# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_details_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'ordering': ['username']},
        ),
        migrations.RemoveField(
            model_name='details',
            name='user',
        ),
    ]
