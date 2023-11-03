from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def get_place(request, place_id):
    obj_place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    place = {'title': obj_place.title,
             'imgs': [img.image.url for img in obj_place.images.all() if img.image],
             'description_short': obj_place.short_description,
             'description_long': obj_place.long_description,
             'coordinates': {'lng': obj_place.coordinates_lng, 'lat': obj_place.coordinates_lat}}
    return JsonResponse(place, safe=False, json_dumps_params={'ensure_ascii': False})


def show_main_page(request):
    geojson_places = {
        'type': 'FeatureCollection',
        'features': []
    }

    places = Place.objects.all()
    for place in places.iterator():
        geojson_places['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.coordinates_lng, place.coordinates_lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('get_place', args=(place.id, ))
                }
            }
        )

    context = {'geojson_places': geojson_places}
    return render(request, 'index.html', context)
