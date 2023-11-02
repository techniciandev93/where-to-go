from django.core.management.base import BaseCommand
from places.services import loading_place


class Command(BaseCommand):
    help = 'Команда для загрузки мест из json'

    def handle(self, *args, **options):
        loading_place(options['place_json'])

    def add_arguments(self, parser):
        parser.add_argument('place_json', type=str, help='Укажите url json')
