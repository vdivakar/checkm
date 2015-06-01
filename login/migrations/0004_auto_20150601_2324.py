# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150531_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'ordering': ['username']},
        ),
        migrations.RenameField(
            model_name='details',
            old_name='teamname',
            new_name='username',
        ),
        migrations.AddField(
            model_name='details',
            name='team_points',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='que_data',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
