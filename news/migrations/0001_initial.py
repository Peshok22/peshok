# Generated by Django 4.1.1 on 2022-09-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название статьи')),
                ('anons', models.CharField(max_length=250, verbose_name='анонс статьи')),
                ('full_text', models.TextField(verbose_name='текст статьи')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
