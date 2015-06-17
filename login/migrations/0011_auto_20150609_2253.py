# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20150609_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='right',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attempt',
            name='unat',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attempt',
            name='wrong',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
