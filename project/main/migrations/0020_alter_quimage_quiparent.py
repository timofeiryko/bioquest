# Generated by Django 3.2.6 on 2021-10-24 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20211020_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quimage',
            name='quiparent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quimage', to='main.question'),
        ),
    ]