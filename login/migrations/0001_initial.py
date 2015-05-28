# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member1', models.CharField(max_length=100)),
                ('member2', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('teamname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['teamname'],
            },
            bases=(models.Model,),
        ),
    ]
