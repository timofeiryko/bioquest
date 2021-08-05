from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['name']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    topics = models.ManyToManyField(Topic, blank=True, related_name='ts')

    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'slug': self.slug})

class Question(models.Model):
    id = models.AutoField
    year = models.IntegerField('Год')
    stage = models.CharField('Олимпиада', max_length=100)
    grade = models.IntegerField('Класс')
    part = models.IntegerField('Часть')
    number = models.IntegerField('Номер')
    text = models.TextField('Текст вопроса')

    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    imageA1 = models.ImageField(blank=True)
    imageA2 = models.ImageField(blank=True)
    imageA3 = models.ImageField(blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='qs')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']

    def __str__(self):
        clear_id = str(self.text)[:30] + '... ' + str (self.comment)[:20] + '...'
        return clear_id
