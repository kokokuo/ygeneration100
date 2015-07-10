# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facewall', '0002_auto_20150710_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinequestion',
            name='gender',
            field=models.BooleanField(default=None, choices=[(True, b'\xe7\x94\xb7\xe6\x80\xa7'), (False, b'\xe5\xa5\xb3\xe6\x80\xa7')]),
            preserve_default=True,
        ),
    ]
