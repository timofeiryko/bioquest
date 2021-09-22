# Generated by Django 3.2.6 on 2021-09-22 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210923_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main.question'),
        ),
    ]
