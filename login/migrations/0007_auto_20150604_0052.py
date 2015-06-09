# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20150604_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='team_points',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
