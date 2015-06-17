# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20150613_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='answer',
            field=models.ForeignKey(to='login.answered'),
            preserve_default=True,
        ),
    ]
