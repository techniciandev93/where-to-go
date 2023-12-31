# Generated by Django 3.2.22 on 2023-10-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description_short', models.CharField(max_length=300, verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Полное описание')),
                ('coordinates_lng', models.FloatField(verbose_name='Долгота')),
                ('coordinates_lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
