# Generated by Django 3.2.22 on 2023-11-01 12:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20231101_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
    ]
