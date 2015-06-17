# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20150609_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='right',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='wrong',
        ),
        migrations.AlterField(
            model_name='attempt',
            name='unat',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
