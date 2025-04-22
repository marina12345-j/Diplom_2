import allure
import requests
from data import UsersData
from helpers import *
from urls import Urls


class TestAuthentication:
    @allure.title('Проверка успешной аутентификации пользователя при передаче валидных кредов созданного аккаунта')
    @allure.description('Аккаунт для проверки создается фикстурой перед тестом и удаляется после. '
                        'В ответе проверяются код и тело, в том числе получение accessToken и refreshToken')
    def test_auth_existing_account_success(self, new_user_creature_and_delete):
        payload = new_user_creature_and_delete[0]
        response = requests.post(Urls.user_auth, data=payload)
        deserial= response.json()
        assert response.status_code == 200
        assert deserial['success'] is True #deserials
        assert 'accessToken' in deserial.keys()
        assert 'refreshToken' in deserial.keys()
        assert deserial['user']['email'] == new_user_creature_and_delete[0]['email']
        assert deserial['user']['name'] == new_user_creature_and_delete[0]['name']

    @allure.title('Проверка ответа на запрос аутентификации с незарегистрированным email')
    def test_auth_with_wrong_login_expected_error(self):
        payload = {
            'email': generate_random_password(),
            'password': UsersData.password,
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}

    @allure.title('Проверка ответа на запрос аутентификации с неверным паролем')
    def test_auth_with_wrong_passwd_expected_error(self):
        payload = {
            'email': UsersData.email,
            'password': generate_random_password(),
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}