from helpers import *


class UsersData:
    email = 'jmailova_praktikum_2025@ya.ru'
    password = 'brains'
    username = 'Marina'

    credentials_with_empty_field = [
        {'email': '',
         'password': generate_random_password(),
         'name': generate_random_username()
         },
        {'email': generate_random_email(),
         'password': '',
         'name': generate_random_username()
         },
        {'email': generate_random_email(),
         'password': generate_random_password(),
         'name': ''
         }
    ]


class IngredientData:
    burger_1 = ['61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa6e', '61c0c5a71d1f82001bdaaa79']

    burger_2 = ['61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa6c',
                '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa7a']

    invalid_hash_ingredient = '61c0c5a71d1f82001bdaaa'