# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_que_data_lock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('right', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('unat', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='details',
            name='answered',
            field=models.ForeignKey(default=0, to='login.Attempt'),
            preserve_default=True,
        ),
    ]
