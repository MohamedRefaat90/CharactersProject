import json
from django.core.management.base import BaseCommand

from Pokemons.models import Pokemon

class Command(BaseCommand):
    help = 'Load pokemons from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to load pokemons from')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                name = item['name']['english']
                description = item['description']
                image = item['image']['hires']
                species = item['species']
                type_list = item['type']

                Pokemon.objects.create(
                    name=name,
                    description=description,
                    image=image,
                    species=species,
                    type=type_list
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded pokemons from JSON file'))