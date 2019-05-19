# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.core.urlresolvers import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    bg = models.CharField(max_length=255, verbose_name="Фон")
    has_music = models.BooleanField(default=True, verbose_name="Есть ли музыка")
    type_user = models.CharField(max_length=255, default="")


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Текст новости")
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    author = models.CharField(max_length=255, default="Админ")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.title])
    

class Chat(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    type_message = models.IntegerField(choices=TYPES, default=1, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)


class Anketa(models.Model):
    title = models.TextField(verbose_name="Вопрос", default="")


class Answers(models.Model):
    one = models.BooleanField(default=False,
                              verbose_name="Если у Вас не клеится работа, Вы способны все скомкать, порвать, бросить в корзину, а затем всплакнут?")
    two = models.BooleanField(default=False, verbose_name="Когда Вы устали, любая мелкая неприятность может довести Вас до крика или до слез?")
    three = models.BooleanField(default=False, verbose_name=" Вы часто склонны сомневаться, получится ли у Вас какое-либо дело, хотя у других подобные сомнения не возникают?")
    four = models.BooleanField(default=False, verbose_name="Вам не приходилось удивляться, почему Вы так удачно выполнили задуманное, хотя заранее обрекали свой план на провал ?")
    five = models.BooleanField(default=False, verbose_name="Никогда Вы не чувствуете себя столь комфортно, как оставшись в одиночеств?")
    six = models.BooleanField(default=False, verbose_name="Вам редко бывает скучно в одиночестве, поскольку есть много интересных дел: книги, компьютер, коллекция почтовых марок?")
    seven = models.BooleanField(default=False, verbose_name="Вы замечали, что настроение у Вас легко меняется в течение дня?")
    eight = models.BooleanField(default=False, verbose_name="Ваша жизнь похожа на сплошную череду полос везения и неудач?")
    nine = models.BooleanField(default=False, verbose_name="Последнее время Вы чувствуете себя усталым, беспомощным, бесполезным и никому не нужным неудачником?")
    ten = models.BooleanField(default=False, verbose_name=" Вы не склонны считать, что Ваша жизнь могла бы сложиться намного успешнее, если бы судьба была к Вам благосклоннее ?")
    eleven = models.BooleanField(default=False, verbose_name="Вас трудно вывести из себя, но уж если это кому-то удалось, Вы не успокоитесь слишком скоро?")
    twelve = models.BooleanField(default=False, verbose_name="Случается, что какой-нибудь вопрос или проблема надолго выводят Вас из спокойного расположения духа?")
    thirteen = models.BooleanField(default=False, verbose_name="Вы легко справились бы с обязанностями Вашего начальника, причем возможно, у Вас получилось бы лучше?")
    fourteen = models.BooleanField(default=False, verbose_name="Вам, возможно, не хватает лишь самого малого, чтобы добиться славы и почета ?")
    fiveteen = models.BooleanField(default=False, verbose_name="Вы мягкий и податливый человек, который легко поддается чужому влиянию?")
    sixteen = models.BooleanField(default=False, verbose_name="Вас нелегко увлечь новой идеей, уговорить отправиться в путешествие, упросить дать свое согласие на участие в авантюре?")
    seventeen = models.BooleanField(default=False, verbose_name="Вас не особенно утомляет работа, требующая внимания, психического напряжения, ответственности?")
    eighteen = models.BooleanField(default=False, verbose_name="После того, как на Вас накричал шеф, Вы долго пытаетесь вспомнить, за что, собственно, он Вас разносил?")
    nineteen = models.BooleanField(default=False, verbose_name="Вам не приходится серьезно опасаться за свое здоровье, а быть может, и жизнь?")
    twenty = models.BooleanField(default=False, verbose_name="Другие готовы верить в Вас более, чем Вы верите в себя?")
    twentyone = models.BooleanField(default=False, verbose_name="Часто, несмотря на очевидные преимущества одного из возможных вариантов, Вы медлите с принятием решения?")
    twentytwo = models.BooleanField(default=False, verbose_name="Вы хорошо знаете, что черная кошка вполне безобидна, но появление ее на Вашем пути способно Вас не на шутку встревожить?")
    twentythree = models.BooleanField(default=False, verbose_name="В шумной компании Вам не по себе, и лучше бы посидеть в уголке, полистывая альбом с фотографиями?")
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
