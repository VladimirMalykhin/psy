# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-19 14:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psyho_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=b'', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.BooleanField(default=False, verbose_name=b'\xd0\x95\xd1\x81\xd0\xbb\xd0\xb8 \xd1\x83 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb5 \xd0\xba\xd0\xbb\xd0\xb5\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0, \xd0\x92\xd1\x8b \xd1\x81\xd0\xbf\xd0\xbe\xd1\x81\xd0\xbe\xd0\xb1\xd0\xbd\xd1\x8b \xd0\xb2\xd1\x81\xd0\xb5 \xd1\x81\xd0\xba\xd0\xbe\xd0\xbc\xd0\xba\xd0\xb0\xd1\x82\xd1\x8c, \xd0\xbf\xd0\xbe\xd1\x80\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c, \xd0\xb1\xd1\x80\xd0\xbe\xd1\x81\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2 \xd0\xba\xd0\xbe\xd1\x80\xd0\xb7\xd0\xb8\xd0\xbd\xd1\x83, \xd0\xb0 \xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbc \xd0\xb2\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd0\xba\xd0\xbd\xd1\x83\xd1\x82?')),
                ('two', models.BooleanField(default=False, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb3\xd0\xb4\xd0\xb0 \xd0\x92\xd1\x8b \xd1\x83\xd1\x81\xd1\x82\xd0\xb0\xd0\xbb\xd0\xb8, \xd0\xbb\xd1\x8e\xd0\xb1\xd0\xb0\xd1\x8f \xd0\xbc\xd0\xb5\xd0\xbb\xd0\xba\xd0\xb0\xd1\x8f \xd0\xbd\xd0\xb5\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82 \xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xb4\xd0\xbe \xd0\xba\xd1\x80\xd0\xb8\xd0\xba\xd0\xb0 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xb4\xd0\xbe \xd1\x81\xd0\xbb\xd0\xb5\xd0\xb7?')),
                ('three', models.BooleanField(default=False, verbose_name=b' \xd0\x92\xd1\x8b \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xbe \xd1\x81\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b \xd1\x81\xd0\xbe\xd0\xbc\xd0\xbd\xd0\xb5\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f, \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f \xd0\xbb\xd0\xb8 \xd1\x83 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xba\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb5-\xd0\xbb\xd0\xb8\xd0\xb1\xd0\xbe \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe, \xd1\x85\xd0\xbe\xd1\x82\xd1\x8f \xd1\x83 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xb8\xd1\x85 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb1\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbc\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb5 \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd1\x8e\xd1\x82?')),
                ('four', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbc \xd0\xbd\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb8\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c \xd1\x83\xd0\xb4\xd0\xb8\xd0\xb2\xd0\xbb\xd1\x8f\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f, \xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd0\xbc\xd1\x83 \xd0\x92\xd1\x8b \xd1\x82\xd0\xb0\xd0\xba \xd1\x83\xd0\xb4\xd0\xb0\xd1\x87\xd0\xbd\xd0\xbe \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xb7\xd0\xb0\xd0\xb4\xd1\x83\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5, \xd1\x85\xd0\xbe\xd1\x82\xd1\x8f \xd0\xb7\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb5\xd0\xba\xd0\xb0\xd0\xbb\xd0\xb8 \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xbf\xd0\xbb\xd0\xb0\xd0\xbd \xd0\xbd\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbb ?')),
                ('five', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb3\xd0\xb4\xd0\xb0 \xd0\x92\xd1\x8b \xd0\xbd\xd0\xb5 \xd1\x87\xd1\x83\xd0\xb2\xd1\x81\xd1\x82\xd0\xb2\xd1\x83\xd0\xb5\xd1\x82\xd0\xb5 \xd1\x81\xd0\xb5\xd0\xb1\xd1\x8f \xd1\x81\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c \xd0\xba\xd0\xbe\xd0\xbc\xd1\x84\xd0\xbe\xd1\x80\xd1\x82\xd0\xbd\xd0\xbe, \xd0\xba\xd0\xb0\xd0\xba \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd1\x88\xd0\xb8\xd1\x81\xd1\x8c \xd0\xb2 \xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xbe\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2?')),
                ('six', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbc \xd1\x80\xd0\xb5\xd0\xb4\xd0\xba\xd0\xbe \xd0\xb1\xd1\x8b\xd0\xb2\xd0\xb0\xd0\xb5\xd1\x82 \xd1\x81\xd0\xba\xd1\x83\xd1\x87\xd0\xbd\xd0\xbe \xd0\xb2 \xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xbe\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5, \xd0\xbf\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd1\x83 \xd0\xb5\xd1\x81\xd1\x82\xd1\x8c \xd0\xbc\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb8\xd0\xbd\xd1\x82\xd0\xb5\xd1\x80\xd0\xb5\xd1\x81\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xb4\xd0\xb5\xd0\xbb: \xd0\xba\xd0\xbd\xd0\xb8\xd0\xb3\xd0\xb8, \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd1\x8c\xd1\x8e\xd1\x82\xd0\xb5\xd1\x80, \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85 \xd0\xbc\xd0\xb0\xd1\x80\xd0\xbe\xd0\xba?')),
                ('seven', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b \xd0\xb7\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb8, \xd1\x87\xd1\x82\xd0\xbe \xd0\xbd\xd0\xb0\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x83 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xbb\xd0\xb5\xd0\xb3\xd0\xba\xd0\xbe \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8f\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb2 \xd1\x82\xd0\xb5\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbd\xd1\x8f?')),
                ('eight', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb7\xd0\xbd\xd1\x8c \xd0\xbf\xd0\xbe\xd1\x85\xd0\xbe\xd0\xb6\xd0\xb0 \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbf\xd0\xbb\xd0\xbe\xd1\x88\xd0\xbd\xd1\x83\xd1\x8e \xd1\x87\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd1\x83 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbe\xd1\x81 \xd0\xb2\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb8 \xd0\xbd\xd0\xb5\xd1\x83\xd0\xb4\xd0\xb0\xd1\x87?')),
                ('nine', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\x92\xd1\x8b \xd1\x87\xd1\x83\xd0\xb2\xd1\x81\xd1\x82\xd0\xb2\xd1\x83\xd0\xb5\xd1\x82\xd0\xb5 \xd1\x81\xd0\xb5\xd0\xb1\xd1\x8f \xd1\x83\xd1\x81\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8b\xd0\xbc, \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd0\xbd\xd1\x8b\xd0\xbc, \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5\xd0\xb7\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xb8 \xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbc\xd1\x83 \xd0\xbd\xd0\xb5 \xd0\xbd\xd1\x83\xd0\xb6\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xbd\xd0\xb5\xd1\x83\xd0\xb4\xd0\xb0\xd1\x87\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbc?')),
                ('ten', models.BooleanField(default=False, verbose_name=b' \xd0\x92\xd1\x8b \xd0\xbd\xd0\xb5 \xd1\x81\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b \xd1\x81\xd1\x87\xd0\xb8\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c, \xd1\x87\xd1\x82\xd0\xbe \xd0\x92\xd0\xb0\xd1\x88\xd0\xb0 \xd0\xb6\xd0\xb8\xd0\xb7\xd0\xbd\xd1\x8c \xd0\xbc\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0 \xd0\xb1\xd1\x8b \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb8\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xbc\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x83\xd1\x81\xd0\xbf\xd0\xb5\xd1\x88\xd0\xbd\xd0\xb5\xd0\xb5, \xd0\xb5\xd1\x81\xd0\xbb\xd0\xb8 \xd0\xb1\xd1\x8b \xd1\x81\xd1\x83\xd0\xb4\xd1\x8c\xd0\xb1\xd0\xb0 \xd0\xb1\xd1\x8b\xd0\xbb\xd0\xb0 \xd0\xba \xd0\x92\xd0\xb0\xd0\xbc \xd0\xb1\xd0\xbb\xd0\xb0\xd0\xb3\xd0\xbe\xd1\x81\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb5\xd0\xb5 ?')),
                ('eleven', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x81 \xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xbe \xd0\xb2\xd1\x8b\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd0\xb8\xd0\xb7 \xd1\x81\xd0\xb5\xd0\xb1\xd1\x8f, \xd0\xbd\xd0\xbe \xd1\x83\xd0\xb6 \xd0\xb5\xd1\x81\xd0\xbb\xd0\xb8 \xd1\x8d\xd1\x82\xd0\xbe \xd0\xba\xd0\xbe\xd0\xbc\xd1\x83-\xd1\x82\xd0\xbe \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c, \xd0\x92\xd1\x8b \xd0\xbd\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbf\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb8\xd1\x82\xd0\xb5\xd1\x81\xd1\x8c \xd1\x81\xd0\xbb\xd0\xb8\xd1\x88\xd0\xba\xd0\xbe\xd0\xbc \xd1\x81\xd0\xba\xd0\xbe\xd1\x80\xd0\xbe?')),
                ('twelve', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbb\xd1\x83\xd1\x87\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f, \xd1\x87\xd1\x82\xd0\xbe \xd0\xba\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb9-\xd0\xbd\xd0\xb8\xd0\xb1\xd1\x83\xd0\xb4\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe \xd0\xb2\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x8f\xd1\x82 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xb8\xd0\xb7 \xd1\x81\xd0\xbf\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb9\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80\xd0\xb0\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb4\xd1\x83\xd1\x85\xd0\xb0?')),
                ('thirteen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b \xd0\xbb\xd0\xb5\xd0\xb3\xd0\xba\xd0\xbe \xd1\x81\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x81\xd1\x8c \xd0\xb1\xd1\x8b \xd1\x81 \xd0\xbe\xd0\xb1\xd1\x8f\xd0\xb7\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8f\xd0\xbc\xd0\xb8 \xd0\x92\xd0\xb0\xd1\x88\xd0\xb5\xd0\xb3\xd0\xbe \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0, \xd0\xbf\xd1\x80\xd0\xb8\xd1\x87\xd0\xb5\xd0\xbc \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe, \xd1\x83 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c \xd0\xb1\xd1\x8b \xd0\xbb\xd1\x83\xd1\x87\xd1\x88\xd0\xb5?')),
                ('fourteen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbc, \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe, \xd0\xbd\xd0\xb5 \xd1\x85\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xbb\xd0\xb8\xd1\x88\xd1\x8c \xd1\x81\xd0\xb0\xd0\xbc\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbc\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xbe, \xd1\x87\xd1\x82\xd0\xbe\xd0\xb1\xd1\x8b \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb8\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd1\x81\xd0\xbb\xd0\xb0\xd0\xb2\xd1\x8b \xd0\xb8 \xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0 ?')),
                ('fiveteen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b \xd0\xbc\xd1\x8f\xd0\xb3\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xbb\xd0\xb8\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x87\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xba, \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b\xd0\xb9 \xd0\xbb\xd0\xb5\xd0\xb3\xd0\xba\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb4\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd1\x87\xd1\x83\xd0\xb6\xd0\xbe\xd0\xbc\xd1\x83 \xd0\xb2\xd0\xbb\xd0\xb8\xd1\x8f\xd0\xbd\xd0\xb8\xd1\x8e?')),
                ('sixteen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xba\xd0\xbe \xd1\x83\xd0\xb2\xd0\xbb\xd0\xb5\xd1\x87\xd1\x8c \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xb8\xd0\xb4\xd0\xb5\xd0\xb5\xd0\xb9, \xd1\x83\xd0\xb3\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb8\xd1\x82\xd1\x8c \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb2 \xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd0\xb5, \xd1\x83\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x81\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0 \xd1\x83\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd0\xb5 \xd0\xb2 \xd0\xb0\xd0\xb2\xd0\xb0\xd0\xbd\xd1\x82\xd1\x8e\xd1\x80\xd0\xb5?')),
                ('seventeen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb5 \xd0\xbe\xd1\x81\xd0\xbe\xd0\xb1\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe \xd1\x83\xd1\x82\xd0\xbe\xd0\xbc\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x82\xd1\x80\xd0\xb5\xd0\xb1\xd1\x83\xd1\x8e\xd1\x89\xd0\xb0\xd1\x8f \xd0\xb2\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f, \xd0\xbf\xd1\x81\xd0\xb8\xd1\x85\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd1\x8f\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f, \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8?')),
                ('eighteen', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb3\xd0\xbe, \xd0\xba\xd0\xb0\xd0\xba \xd0\xbd\xd0\xb0 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb0\xd0\xba\xd1\x80\xd0\xb8\xd1\x87\xd0\xb0\xd0\xbb \xd1\x88\xd0\xb5\xd1\x84, \xd0\x92\xd1\x8b \xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb3\xd0\xbe \xd0\xbf\xd1\x8b\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82\xd0\xb5\xd1\x81\xd1\x8c \xd0\xb2\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbd\xd0\xb8\xd1\x82\xd1\x8c, \xd0\xb7\xd0\xb0 \xd1\x87\xd1\x82\xd0\xbe, \xd1\x81\xd0\xbe\xd0\xb1\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe, \xd0\xbe\xd0\xbd \xd0\x92\xd0\xb0\xd1\x81 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xbe\xd1\x81\xd0\xb8\xd0\xbb?')),
                ('nineteen', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbc \xd0\xbd\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb8\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f \xd1\x81\xd0\xb5\xd1\x80\xd1\x8c\xd0\xb5\xd0\xb7\xd0\xbd\xd0\xbe \xd0\xbe\xd0\xbf\xd0\xb0\xd1\x81\xd0\xb0\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb7\xd0\xb0 \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb2\xd1\x8c\xd0\xb5, \xd0\xb0 \xd0\xb1\xd1\x8b\xd1\x82\xd1\x8c \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82, \xd0\xb8 \xd0\xb6\xd0\xb8\xd0\xb7\xd0\xbd\xd1\x8c?')),
                ('twenty', models.BooleanField(default=False, verbose_name=b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xb8\xd0\xb5 \xd0\xb3\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b \xd0\xb2\xd0\xb5\xd1\x80\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xb1\xd0\xbe\xd0\xbb\xd0\xb5\xd0\xb5, \xd1\x87\xd0\xb5\xd0\xbc \xd0\x92\xd1\x8b \xd0\xb2\xd0\xb5\xd1\x80\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xb2 \xd1\x81\xd0\xb5\xd0\xb1\xd1\x8f?')),
                ('twentyone', models.BooleanField(default=False, verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81\xd1\x82\xd0\xbe, \xd0\xbd\xd0\xb5\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd1\x8f \xd0\xbd\xd0\xb0 \xd0\xbe\xd1\x87\xd0\xb5\xd0\xb2\xd0\xb8\xd0\xb4\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb8\xd0\xbc\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0 \xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb8\xd0\xb7 \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd0\xbe\xd0\xb2, \xd0\x92\xd1\x8b \xd0\xbc\xd0\xb5\xd0\xb4\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x81 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb5\xd0\xbc \xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f?')),
                ('twentytwo', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b \xd1\x85\xd0\xbe\xd1\x80\xd0\xbe\xd1\x88\xd0\xbe \xd0\xb7\xd0\xbd\xd0\xb0\xd0\xb5\xd1\x82\xd0\xb5, \xd1\x87\xd1\x82\xd0\xbe \xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xbe\xd1\x88\xd0\xba\xd0\xb0 \xd0\xb2\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5 \xd0\xb1\xd0\xb5\xd0\xb7\xd0\xbe\xd0\xb1\xd0\xb8\xd0\xb4\xd0\xbd\xd0\xb0, \xd0\xbd\xd0\xbe \xd0\xbf\xd0\xbe\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb5\xd0\xb5 \xd0\xbd\xd0\xb0 \xd0\x92\xd0\xb0\xd1\x88\xd0\xb5\xd0\xbc \xd0\xbf\xd1\x83\xd1\x82\xd0\xb8 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x81\xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe \xd0\x92\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb5 \xd0\xbd\xd0\xb0 \xd1\x88\xd1\x83\xd1\x82\xd0\xba\xd1\x83 \xd0\xb2\xd1\x81\xd1\x82\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb6\xd0\xb8\xd1\x82\xd1\x8c?')),
                ('twentythree', models.BooleanField(default=False, verbose_name=b'\xd0\x92 \xd1\x88\xd1\x83\xd0\xbc\xd0\xbd\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8 \xd0\x92\xd0\xb0\xd0\xbc \xd0\xbd\xd0\xb5 \xd0\xbf\xd0\xbe \xd1\x81\xd0\xb5\xd0\xb1\xd0\xb5, \xd0\xb8 \xd0\xbb\xd1\x83\xd1\x87\xd1\x88\xd0\xb5 \xd0\xb1\xd1\x8b \xd0\xbf\xd0\xbe\xd1\x81\xd0\xb8\xd0\xb4\xd0\xb5\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x83\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xba\xd0\xb5, \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x8b\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc \xd1\x81 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f\xd0\xbc\xd0\xb8?')),
                ('psyhotype', models.CharField(default=b'', max_length=255)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('description', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8')),
                ('image', models.ImageField(blank=True, upload_to=b'image/%Y/%m/%d/', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0')),
                ('author', models.CharField(default=b'\xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type_message', models.IntegerField(choices=[(1, b'Admin'), (2, b'Client')], default=1, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_readed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.FileField(upload_to=b'tasks/')),
                ('answer', models.FileField(default=0, upload_to=b'answers/')),
                ('is_readed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, b'\xd0\x9d\xd0\xb5 \xd1\x81\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe'), (2, b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd1\x8f\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f'), (3, b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbe')], default=1, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81')),
                ('comment', models.TextField(default=b'')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80')),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('upload', models.FileField(default=0, upload_to=b'media/')),
                ('is_readed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='type_user',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
