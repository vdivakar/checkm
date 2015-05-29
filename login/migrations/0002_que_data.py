# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='que_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qno', models.IntegerField()),
                ('que', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
