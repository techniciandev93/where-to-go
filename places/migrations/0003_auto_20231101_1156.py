# Generated by Django 3.2.22 on 2023-11-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20231031_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
