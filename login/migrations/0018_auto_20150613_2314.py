# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_auto_20150613_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answered',
            name='attempt',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
