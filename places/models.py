from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', unique=True)
    description_short = HTMLField(max_length=300, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    coordinates_lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    position = models.IntegerField(verbose_name='Позиция', default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.position} {self.place.title}'

    def get_preview_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" style="max-width:200px; max-height:200px"/>')
        return 'Здесь будет изображение'

    get_preview_image.short_description = 'Вывод изображения'
