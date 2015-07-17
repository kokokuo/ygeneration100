# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facewall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinequestion',
            name='nickname',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
