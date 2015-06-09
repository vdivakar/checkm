# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_que_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='que_data',
            options={'ordering': ['qno']},
        ),
        migrations.AlterField(
            model_name='que_data',
            name='points',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
    ]
