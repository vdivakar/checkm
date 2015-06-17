# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150609_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='que_data',
            name='lock',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
