# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facewall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinequestion',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='onlinequestion',
            name='gender',
            field=models.BooleanField(choices=[(True, b'\xe7\x94\xb7\xe6\x80\xa7'), (False, b'\xe5\xa5\xb3\xe6\x80\xa7')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='onlinequestion',
            name='topic_num',
            field=models.CharField(default='Ques1', max_length=10),
            preserve_default=False,
        ),
    ]
