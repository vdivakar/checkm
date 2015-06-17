# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20150613_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='answer',
            field=models.ForeignKey(blank=True, to='login.answered', null=True),
            preserve_default=True,
        ),
    ]
