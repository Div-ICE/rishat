# Generated by Django 4.1.3 on 2022-11-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите название', max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(help_text='Опишите товар', max_length=3000, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
