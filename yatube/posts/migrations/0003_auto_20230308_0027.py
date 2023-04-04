# Generated by Django 2.2.6 on 2023-03-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230221_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'сообщество', 'verbose_name_plural': 'сообщества'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'запись', 'verbose_name_plural': 'записи'},
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(max_length=400, verbose_name='Описание сообщества'),
        ),
    ]