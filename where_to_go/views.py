from django.shortcuts import render
from django.urls import reverse
from places.models import Place


def show_main_page(request):
    places_geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

    places = Place.objects.all()
    for place in places:
        places_geojson['features'].append(
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

    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)
