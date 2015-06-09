# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_details_user'),
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
    ]
