# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facewall', '0003_auto_20150710_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinequestion',
            name='birth_day',
            field=models.IntegerField(default=12, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinequestion',
            name='birth_month',
            field=models.IntegerField(default=12, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinequestion',
            name='birth_year',
            field=models.IntegerField(default=2001, max_length=4),
            preserve_default=False,
        ),
    ]
