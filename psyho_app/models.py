# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from .choices import *

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	bg = models.CharField(max_length=255, verbose_name="Фон")
	has_music = models.BooleanField(default=True, verbose_name="Есть ли музыка")

class Chat(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	type_message = models.IntegerField(choices=TYPES, default=1, verbose_name="Тип")
	created_at = models.DateTimeField(auto_now_add=True)
	is_readed = models.BooleanField(default=False)


class Book(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

class Music(models.Model):
	user = models.ForeignKey(User)
	author = models.CharField(max_length=255, verbose_name="Автор")
	title = models.CharField(max_length=255, verbose_name="Название")
	upload = models.FileField(upload_to='media/', default=0)
	is_readed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)


class Homework(models.Model):
	task = models.FileField(upload_to='tasks/')
	answer = models.FileField(upload_to='answers/', default=0)
	user = models.ForeignKey(User)
	is_readed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUSES, default=1, verbose_name="Статус")
	comment = models.TextField(default="")