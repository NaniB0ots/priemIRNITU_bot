# Generated by Django 3.1.7 on 2021-03-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='contains_categories',
        ),
        migrations.AddField(
            model_name='category',
            name='contains_questions',
            field=models.BooleanField(default=True, verbose_name='Содержит вопросы (иначе категории)'),
        ),
    ]