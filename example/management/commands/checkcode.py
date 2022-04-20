import json
from json import JSONDecodeError

from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('code')

    def handle(self, *args, **options):

        code = options['code']

        try:
            with open('codes.json', 'r') as file:
                data = json.load(file)
        except JSONDecodeError:

            raise CommandError('Ошибка чтения файла, возможно он пуст')

        except FileNotFoundError:
            raise CommandError('Файл с кодами не найден')

        found = False
        for group in data:
            final_group = group
            codes = data[group]
            if code in codes:
                found = True
                break
        if found:
            self.stdout.write(self.style.SUCCESS(f'Код существует, группа: {final_group}'))
        else:
            self.stdout.write(self.style.WARNING(f'Код не существует'))
