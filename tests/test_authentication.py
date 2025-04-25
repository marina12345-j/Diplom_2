import allure
import pytest
import requests
from data import *
from urls import Urls


class TestAuthentication:
    @allure.title('Проверка авторизации пользователя с рандомными кредами')

    def test_auth_existing_account_success(self, new_user_creature_and_delete):
        payload = new_user_creature_and_delete[0]
        with allure.step('Отправляем запрос с рандомными кредами на подтверждение успешной авторизации '
                         'пользователя, ожидаем ответ: код 200, в теле ответа email и имя пользователя'):
            response = requests.post(Urls.user_auth, data=payload)
            deserial= response.json()
        assert response.status_code == 200
        assert deserial['success'] is True
        assert 'accessToken' in deserial.keys()
        assert 'refreshToken' in deserial.keys()
        assert deserial['user']['email'] == new_user_creature_and_delete[0]['email']
        assert deserial['user']['name'] == new_user_creature_and_delete[0]['name']


    @allure.title('Проверка авторизации с незарегистрированным email, с неверным паролем.'
                 'С помощью параметризации выполняем два теста')
    @pytest.mark.parametrize('emai_password', UsersData.email_password_only)
    def test_auth_with_wrong_login_expected_error(self, emai_password):
        with allure.step('Отправляем запрос с невалидными тестовыми данными на '
                         'подтверждение успешной авторизации пользователя,'
                         'ожидаем ответ: код 401, тело ответа:'):
            response = requests.post(Urls.user_auth, data=emai_password)
        assert response.status_code == 401 and response.json() == negative_authentication_text