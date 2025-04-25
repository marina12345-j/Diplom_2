from helpers import *

# Авторизация текст ответов сервера на запросы
negative_authentication_text = {"success": False, "message": "email or password are incorrect"}

# Получение списка заказов
negative_order_list = {'success': False, 'message': 'You should be authorised'}

# Регистрация пользователя
#not_filled =  {'success': False, 'message': 'Email, password and name are required fields'}
no_email = {'success': False, 'message': 'User already exists'}


# Создание заказа текст ответов сервера на запросы
class CreateOrder:
    user_not_logged = {'success': False, 'message': 'Email, password and name are required fields'}
    ingredient_must_be_provided = {'success': False, 'message': 'Ingredient ids must be provided'}
    hech_ingredient = {'Internal Server Error'}




class UsersData:
     email = 'jmailova_praktikum_2025@ya.ru'
     password = 'brains'
     username = 'Marina'

     email_password_only = [
        {'email': generate_random_email(),
         'password': 'brains'
         },
        {'email': 'jmailova_praktikum_2025@ya.ru',
         'password': generate_random_password()
         }
         ]

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