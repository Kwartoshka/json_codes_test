from json import JSONDecodeError
import json
from django.core.management import call_command
from django.test import TestCase


# Если файл уже существует и он не пустой, нужно знать стартовые параметры json
def get_start_numbers(filename='codes.json'):
    try:
        with open('codes.json', 'r') as file:
            data = json.load(file)
    except JSONDecodeError:
        data = {}
    except FileNotFoundError:
        data = {}
    start_codes_number = 0
    if data:
        for group in data:
            start_codes_number += len(data[group])
    start_groups_number  = len(data.keys())

    return start_codes_number, start_groups_number


class CommandsTestCase(TestCase):

        def test_createcodes(self):
            parameters = ([10, 'агентства'],
                          [1, 'агентства'],
                          [42, 'avtostop'],
                          [5, 1])

            # количество добавляемых кодов (всего)
            testing_codes_number = 0

            # стартовые значения параметров, если файл уже существует и не пустой
            start_codes_number, start_groups_number = get_start_numbers()

            # добавляемые уникальные группы (всего)
            testing_groups = []

            for case in parameters:

                if case[1] not in testing_groups:
                    testing_groups.append(case[1])
                testing_codes_number += case[0]
                args = case
                opts = {}
                call_command('createcodes', *args, **opts)

            # количество добавляемых уникальных групп (всего)
            testing_groups_number = len(testing_groups)

            with open('codes.json', 'r') as file:
                data = json.load(file)
            codes_number = 0
            for group in data:
                codes_number += len(data[group])
            groups = len(data.keys())

            # проверка, что количество групп добавилось корректно
            self.assertLessEqual(groups, start_groups_number + testing_groups_number)
            # проверка, что количество кодов добавилось корректно
            self.assertEqual(codes_number, start_codes_number + testing_codes_number)

