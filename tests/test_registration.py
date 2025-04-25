import requests
import pytest
import allure
from urls import *
from data import *


class TestRegistration:
    @allure.title('Проверка регистрации пользователя, данные валидны')
    def test_registration_new_account_success_submit(self):
        payload = {
            'email': generate_random_email(),
            'password': generate_random_password(),
            'name': generate_random_username()
        }
        with allure.step('Отправляем запрос на регистрацию пользователя, ожидаем ответ: код 200, в теле ответа email, '
                         'имя'):
            response = requests.post(Urls.user_register, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == payload['email']
        assert deserials['user']['name'] == payload['name']
        access_token = deserials['accessToken']
        requests.delete(Urls.user_delete, headers={'Authorization': access_token})


    @allure.title('Регистрация с незаполненным одним из обязательных полей пользователя'
                 'С помощью параметризации выполняем три теста:'
                        'не заполнено поле — email,'
                        'не заполнено поле - passwd'
                        'не заполнено поле - name.')
    @pytest.mark.parametrize('credentials', UsersData.credentials_with_empty_field)
    def test_registration_one_required_field_is_empty_failed_submit(self, credentials):
        with allure.step('Отправляем запрос на регистрацию пользователя, ожидаем ответ: код 403'):
            response = requests.post(Urls.user_register, data=credentials)
        assert response.status_code == 403 and response.json() == CreateOrder.user_not_logged

    @allure.title('Регистрация пользователя с существующим в базе email')
    def test_registration_login_taken_failed_submit(self):
        payload = {
            'email': UsersData.email,
            'password': generate_random_password(),
            'name': generate_random_username()
        }
        with allure.step('Отправляем запрос на регистрацию пользователя, ожидаем ответ: код 403'):
            response = requests.post(Urls.user_register, data=payload)
        assert response.status_code == 403 and response.json() == no_email
