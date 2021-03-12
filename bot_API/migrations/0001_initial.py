# Generated by Django 3.1.7 on 2021-03-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=60, verbose_name='Название платформы')),
                ('create_bot_url', models.URLField(blank=True, verbose_name='Ссылка на создание бота')),
                ('description', models.TextField(blank=True, verbose_name='Инструкция по созданию бота')),
            ],
            options={
                'verbose_name': 'Платформа чат-бота',
                'verbose_name_plural': 'Платформы чат-ботов',
                'ordering': ['platform'],
            },
        ),
    ]