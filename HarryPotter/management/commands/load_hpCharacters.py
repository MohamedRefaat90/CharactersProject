import json
from django.core.management.base import BaseCommand

from HarryPotter.models import HarryPotterCharacter

class Command(BaseCommand):
    help = 'Load pokemons from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to load pokemons from')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                name = item['name']
                gender = item['gender']
                house = item['house']
                yearOfBirth = item['yearOfBirth']
                ancestry = item['ancestry']
                patronus = item['patronus']
                image = item['image']

                # Check if any field is empty or null   
                if not all([name, gender, house, yearOfBirth, ancestry, patronus, image]):
                    continue
            
                HarryPotterCharacter.objects.create(
                    name = name,
                    gender = gender,
                    house = house,
                    yearOfBirth = yearOfBirth,
                    ancestry = ancestry,
                    patronus = patronus,
                    image = image
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded pokemons from JSON file'))