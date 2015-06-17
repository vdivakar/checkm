# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20150609_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='answered',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Attempt',
        ),
    ]
