# Generated by Django 3.1.7 on 2021-04-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_API', '0008_auto_20210403_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botcommands',
            name='command_type',
            field=models.TextField(choices=[('start', 'Старт'), ('help', 'Помощь'), ('about', 'Описание')], max_length=150, unique=True, verbose_name='Тип команды'),
        ),
    ]
