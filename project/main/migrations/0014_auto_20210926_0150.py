# Generated by Django 3.2.6 on 2021-09-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210924_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='files/', verbose_name='Прикрепленный файл')),
                ('label', models.CharField(blank=True, max_length=500, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Файл к вопросу',
                'verbose_name_plural': 'Файлы к вопросу',
            },
        ),
        migrations.CreateModel(
            name='CoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to='images/', verbose_name='Прикрепленнное изображение')),
                ('label', models.CharField(blank=True, max_length=500, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Иллюстрация к вопросу',
                'verbose_name_plural': 'Иллюстрации к вопросу',
            },
        ),
        migrations.CreateModel(
            name='QuImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to='images/', verbose_name='Прикрепленнное изображение')),
                ('label', models.CharField(blank=True, max_length=500, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Иллюстрация к вопросу',
                'verbose_name_plural': 'Иллюстрации к вопросу',
            },
        ),
        migrations.RemoveField(
            model_name='multipleimage',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='MultipleFile',
        ),
        migrations.DeleteModel(
            name='MultipleImage',
        ),
    ]
