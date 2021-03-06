# MODELS ARE UPDATED! TESTING V7

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import os
# Create your models here.

class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'slug': self.slug})

class Topic(models.Model):
    parent_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name='topics')
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['parent_tag', 'name']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.AutoField
    year = models.IntegerField('Год', null=True)
    stage = models.CharField('Олимпиада', max_length=100, null=True)
    grade = models.IntegerField('Класс', null=True)
    part = models.CharField('Часть', max_length=100, null=True)
    number = models.IntegerField('Номер', null=True)
    text = models.TextField('Текст вопроса', null=True)
    uploaded = models.DateTimeField('Вопрос загружен', auto_now_add=True)
    modified = models.DateTimeField('Изменено', auto_now=True)

    quauthor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='questions',
        verbose_name='Добавил вопрос')
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')
    topics = models.ManyToManyField(Topic, blank=True, related_name='questions')

    class Types(models.TextChoices):
        PART1 = 'P1', ('1 правильный ответ')
        PART2 = 'P2', ('Множественный выбор')
        RELATE = 'REL', ('Соответствие')
        MANY = 'MANY', ('Пункты')
        STR = 'STR', ('Текст')

    class Flags(models.TextChoices):
        CORE = 'CORE', ('ВсОШ')
        EXTRA = 'EXTRA', ('Другие олимпиады')
        COMMUNITY = 'COM', ('От пользователей')
        EXCLUSIVE = 'EXCL', ('Эксклюзив от создателей')

    flag = models.CharField(
        'Коллекция',
        max_length=10,
        choices=Flags.choices,
        default=Flags.CORE,
    )

    type = models.CharField(
        'Тип',
        max_length=4,
        choices=Types.choices,
        default=Types.STR,
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']

    def __str__(self):
        clear_id = str(self.text)[:30]
        return clear_id

class Comment(models.Model):
    parent_question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='comment')
    text = models.TextField('Разбор, комментарии', blank=False)

    coauthor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='comments',
        verbose_name='Добавил разбор')

    uploaded = models.DateTimeField('Вопрос загружен', auto_now_add=True, null=True)
    modified = models.DateTimeField('Изменено', auto_now=True, null=True )

    mark = models.BooleanField('Проверено экспертом', default=False)

    class Meta:
        ordering = ['parent_question']
        verbose_name = 'Разбор'
        verbose_name_plural = 'Разборы'

class QuImage(models.Model):
	quiparent = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='quimage')
	quifile = models.ImageField('Прикрепленнное изображение', blank=True, upload_to='images/')
	quilabel = models.CharField('Подпись', blank=True, max_length=500)

	class Meta:
		verbose_name = 'Иллюстрация к вопросу'
		verbose_name_plural = 'Иллюстрации к вопросу'

	def __str__(self):
		return self.quilabel

class CoImage(models.Model):
	coiparent = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
	coifile = models.ImageField('Прикрепленнное изображение', blank=True, upload_to='images/')
	coilabel = models.CharField('Подпись', blank=True, max_length=500)
	class Meta:
		verbose_name = 'Иллюстрация к рабору'
		verbose_name_plural = 'Иллюстрации к разбору'

	def __str__(self):
		return self.coilabel

class CoFile(models.Model):
	parent = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
	file = models.FileField('Прикрепленный файл', blank=True, upload_to='files/')
	label = models.CharField('Подпись', blank=True, max_length=500)
	class Meta:
		verbose_name = 'Файл к разбору'
		verbose_name_plural = 'Файлы к разбору'
	def __str__(self):
		return self.label
	def filename(self):
		return os.path.basename(self.file.name)


class VarList(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    var = models.TextField('Текст варианта')
    is_right = models.BooleanField('Правильность', default=False)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
        ordering = ['parent_question']

    def __str__(self):
        return self.var

class Relative(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    lettervar = models.TextField('Текст варианта')

    def __str__(self):
        return self.var

    class Meta:
        verbose_name = 'Буква'
        verbose_name_plural = 'Буквы'

class RelInitial(models.Model):
    parrent_relative = models.ForeignKey(Relative, on_delete=models.CASCADE, null=True, blank=True)
    numbervar = models.TextField('Текст варианта')

    class Meta:
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'

    def __str__(self):
        return self.var

class ItemList(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    itemtext = models.TextField('Вопрос')
    itemans = models.TextField('Ответ')
    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'
        ordering = ['parent_question']

    def __str__(self):
        return self.text
