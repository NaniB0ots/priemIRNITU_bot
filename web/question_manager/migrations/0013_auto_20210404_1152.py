# Generated by Django 3.1.7 on 2021-04-04 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0012_auto_20210404_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='contains_questions',
        ),
        migrations.RemoveField(
            model_name='category',
            name='editor',
        ),
        migrations.RemoveField(
            model_name='question',
            name='editor',
        ),
    ]
