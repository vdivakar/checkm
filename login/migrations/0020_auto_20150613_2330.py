# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20150613_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answered',
            name='attempt',
            field=models.IntegerField(default=10000),
            preserve_default=True,
        ),
    ]
