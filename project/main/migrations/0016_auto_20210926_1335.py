# Generated by Django 3.2.6 on 2021-09-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210926_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='parent_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='parent_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
        migrations.AlterField(
            model_name='relinitial',
            name='parrent_relative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.relative'),
        ),
        migrations.AlterField(
            model_name='varlist',
            name='parent_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
    ]
