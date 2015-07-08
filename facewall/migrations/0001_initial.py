# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('contact_email', models.EmailField(max_length=75)),
                ('content', models.TextField(null=True, blank=True)),
                ('face_image', models.ImageField(upload_to=b'upload/picture_story/')),
                ('youtube_url', models.TextField()),
                ('type', models.CharField(max_length=10, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
