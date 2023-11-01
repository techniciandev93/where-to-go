from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_short = models.TextField(max_length=300, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    coordinates_lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    position = models.IntegerField(verbose_name='Позиция', default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
