import string
import random
import json
from json import JSONDecodeError

from django.core.management.base import BaseCommand

def get_or_create_group(data:dict, group=1):
    if group not in data.keys():
        data[group] = []


def get_codes(data:dict):
    codes = []
    for group in data:
        codes += data[group]
    return codes



def create_code(codes, N=6):

    unique = False

    while unique == False:

        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        if code not in codes:
            unique = True

    return code


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)
        parser.add_argument('group')

    def handle(self, *args, **options):
        amount = options['amount']
        group = options['group']


        try:
            with open('codes.json', 'r') as file:
                data = json.load(file)
        except JSONDecodeError:
            data = {}
        except FileNotFoundError:
            data = {}

        with open('codes.json', 'w') as file:

            get_or_create_group(data, group)
            codes = get_codes(data)

            for i in range(1, amount+1):
                code = create_code(codes)
                data[group].append(code)
            json.dump(data, file, ensure_ascii=False, indent=4)
