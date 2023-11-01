from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Place


def get_place(request, place_id):
    obj_place = get_object_or_404(Place, id=place_id)
    place = {'title': obj_place.title,
             'imgs': [img.image.url for img in obj_place.images.all() if img.image],
             'description_short': obj_place.description_short,
             'description_long': obj_place.description_long,
             'coordinates': {'lng': obj_place.coordinates_lng, 'lat': obj_place.coordinates_lat}}
    return JsonResponse(place, safe=False, json_dumps_params={'ensure_ascii': False})
