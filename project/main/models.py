from django.db import models

# Create your models here.

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
    year = models.IntegerField('Год')
    stage = models.CharField('Олимпиада', max_length=100)
    grade = models.IntegerField('Класс')
    part = models.IntegerField('Часть')
    number = models.IntegerField('Номер')
    text = models.TextField('Текст вопроса')

    image1 = models.ImageField('Иллюстрация к вопросу', blank=True)
    image2 = models.ImageField('Иллюстрация к вопросу', blank=True)
    image3 = models.ImageField('Иллюстрация к вопросу', blank=True)
    imageA1 = models.ImageField('Иллюстрация к ответу', blank=True)
    imageA2 = models.ImageField('Иллюстрация к ответу', blank=True)
    imageA3 = models.ImageField('Иллюстрация к ответу', blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')
    topics = models.ManyToManyField(Topic, blank=True, related_name='questions')
    class Types(models.TextChoices):
        PART1 = 'P1', ('1 правильный ответ')
        PART2 = 'P2', ('Множественный выбор')
        RELATE = 'REL', ('Соответствие')
        MANY = 'MANY', ('Пункты')
        STR = 'STR', ('Текст')

    type = models.CharField(
        'Тип',
        max_length=4,
        choices=Types.choices,
        default=Types.STR,
    )

    comment = models.TextField('Разбор, комментарии', blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']

    def __str__(self):
        clear_id = str(self.text)[:30] + '... ' + str (self.comment)[:20] + '...'
        return clear_id

class VarList(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    var = models.CharField('Текст варианта', max_length=200)
    is_right = models.BooleanField('Правильность', default=False)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
        ordering = ['parent_question']

    def __str__(self):
        return self.var

class Relative(models.Model):
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    var = models.CharField('Текст варианта', max_length=200)

    def __str__(self):
        return self.var

    class Meta:
        verbose_name = 'Буква'
        verbose_name_plural = 'Буквы'

class RelInitial(models.Model):
    parrent_relative = models.ForeignKey(Relative, on_delete=models.CASCADE, null=True)
    var = models.CharField('Текст варианта', max_length=200)

    class Meta:
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'

    def __str__(self):
        return self.var
