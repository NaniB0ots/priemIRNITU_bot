# Generated by Django 3.1.7 on 2021-04-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_manager', '0006_auto_20210413_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesthistory',
            name='status',
            field=models.CharField(choices=[('Готово', 'Готово'), ('Не валидно', 'Не валидно'), ('Ожидает', 'Ожидает')], max_length=150, verbose_name='Статус'),
        ),
    ]