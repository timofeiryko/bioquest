# Generated by Django 3.2.6 on 2021-09-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_question_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Год'),
        ),
    ]
