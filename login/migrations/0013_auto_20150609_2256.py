# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20150609_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='answered',
            field=models.ForeignKey(to='login.Attempt'),
            preserve_default=True,
        ),
    ]
