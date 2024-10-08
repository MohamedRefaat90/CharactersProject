import json
from django.core.management.base import BaseCommand
from HarryPotter.models import HarryPotterCharacter

class Command(BaseCommand):
    help = 'Load Harry Potter characters from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to load characters from')

    def handle(self, *args, **options):
        json_file = options['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File {json_file} not found'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format'))
            return

        for item in data:
            name = item.get('name', '')
            gender = item.get('gender', '')
            house = item.get('house', '')
            year_of_birth = item.get('yearOfBirth', None)
            ancestry = item.get('ancestry', '')
            patronus = item.get('patronus', '')
            image = item.get('image', '')

            if not image:
                self.stdout.write(self.style.WARNING(f'Skipped character {name} due to missing image'))
                continue

            HarryPotterCharacter.objects.create(
                name=name,
                gender=gender,
                house=house,
                yearOfBirth=year_of_birth,
                ancestry=ancestry,
                patronus=patronus,
                image=image
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded Harry Potter characters from JSON file'))
