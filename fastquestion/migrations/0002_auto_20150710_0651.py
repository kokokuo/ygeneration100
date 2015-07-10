# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastquestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastquestion',
            name='youtube_url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
