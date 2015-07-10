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
            name='youtube_url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
