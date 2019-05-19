# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from .choices import *

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	bg = models.CharField(max_length=255, verbose_name="Фон")
	has_music = models.BooleanField(default=True, verbose_name="Есть ли музыка")
        type_user = models.CharField(max_length=255, default="")

class Chat(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	type_message = models.IntegerField(choices=TYPES, default=1, verbose_name="Тип")
	created_at = models.DateTimeField(auto_now_add=True)
	is_readed = models.BooleanField(default=False)

class Anketa(models.Model):
    	title = models.TextField(verbose_name="Вопрос", default = "")

class Answers(models.Model):
        one =  models.BooleanField(default=False, verbose_name="?")
	two =  models.BooleanField(default=False, verbose_name="?")
	three =  models.BooleanField(default=False, verbose_name="?")
	four =  models.BooleanField(default=False, verbose_name="?")
	five =  models.BooleanField(default=False, verbose_name="?")
	six =  models.BooleanField(default=False, verbose_name="?")
	seven =  models.BooleanField(default=False, verbose_name="?")
	eight =  models.BooleanField(default=False, verbose_name="?")
	nine =  models.BooleanField(default=False, verbose_name="?")
	ten =  models.BooleanField(default=False, verbose_name="?")
	eleven =  models.BooleanField(default=False, verbose_name="?")
	twelve =  models.BooleanField(default=False, verbose_name="?")
	thirteen =  models.BooleanField(default=False, verbose_name="?")
	fourteen =  models.BooleanField(default=False, verbose_name="?")
	fiveteen =  models.BooleanField(default=False, verbose_name="?")
	sixteen =  models.BooleanField(default=False, verbose_name="?")
	seventeen =  models.BooleanField(default=False, verbose_name="?")
	eighteen =  models.BooleanField(default=False, verbose_name="?")
	nineteen =  models.BooleanField(default=False, verbose_name="?")
	twenty =  models.BooleanField(default=False, verbose_name="?")
	twentyone =  models.BooleanField(default=False, verbose_name="?")
	twentytwo =  models.BooleanField(default=False, verbose_name="?")
	twentythree =  models.BooleanField(default=False, verbose_name="?")
        user = models.ForeignKey(User, default=0)
        psyhotype = models.CharField(max_length=255, default="")




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
