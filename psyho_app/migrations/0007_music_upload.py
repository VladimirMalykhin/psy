# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-27 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psyho_app', '0006_music_is_readed'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='upload',
            field=models.FileField(default=0, upload_to=b'media/'),
        ),
    ]
