import os

from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile

from places.models import Place, Image


def create_place(place):
    obj_place, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={'short_description': place['description_short'],
                  'long_description': place['description_long'],
                  'coordinates_lng': place['coordinates']['lng'],
                  'coordinates_lat': place['coordinates']['lat']}
    )

    for number, img_url in enumerate(place['imgs']):
        response = requests.get(img_url)
        response.raise_for_status()
        file_name = os.path.basename(urlparse(response.url).path)
        file = ContentFile(response.content, name=file_name)
        Image.objects.get_or_create(image=file, place=obj_place, position=number)


def loading_place(url):
    response = requests.get(url)
    response.raise_for_status()
    place = response.json()
    create_place(place)
