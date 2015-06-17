# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20150613_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='answered',
            name='who',
            field=models.CharField(default=b'hey', max_length=100),
            preserve_default=True,
        ),
    ]
