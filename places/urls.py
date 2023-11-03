from django.urls import path

from places import views

urlpatterns = ([
    path('', views.show_main_page),
    path('places/<int:place_id>', views.get_place, name='get_place')
])
