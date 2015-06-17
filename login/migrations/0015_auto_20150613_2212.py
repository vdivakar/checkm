# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20150609_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='answered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attempt', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='details',
            name='answered',
            field=models.ForeignKey(to='login.answered'),
            preserve_default=True,
        ),
    ]
