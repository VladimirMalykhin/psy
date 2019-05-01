# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-26 18:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xbe\xd0\xbd')),
                ('has_music', models.BooleanField(default=True, verbose_name=b'\xd0\x95\xd1\x81\xd1\x82\xd1\x8c \xd0\xbb\xd0\xb8 \xd0\xbc\xd1\x83\xd0\xb7\xd1\x8b\xd0\xba\xd0\xb0')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]