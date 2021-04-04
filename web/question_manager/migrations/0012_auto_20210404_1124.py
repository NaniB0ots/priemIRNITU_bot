# Generated by Django 3.1.7 on 2021-04-04 03:24

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0011_auto_20210404_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_manager.category', verbose_name='Категория'),
        ),
    ]
