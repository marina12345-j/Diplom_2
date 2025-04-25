import allure
import requests

from data import negative_order_list
from helpers import *
from urls import Urls


class TestUserUpdate:
    updated_user_data = {
        'email': generate_random_email(),
        'password': generate_random_password(),
        'name': generate_random_username()
    }

    @allure.title('Проверка ответа на запрос изменения данных пользователя,пользователь зарегистрирован')
    def test_update_user_authenticated_success(self, new_user_creature_and_delete):
        with allure.step('Отправляем запрос на изменение данных  пользователя, ожидаем ответ: код 200, в теле ответа email, '
                         'имя'):
            response = requests.patch(Urls.user_update, headers={
            'Authorization': new_user_creature_and_delete[1]['accessToken']}, data=TestUserUpdate.updated_user_data)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert deserials['user']['email'] == TestUserUpdate.updated_user_data['email']
        assert deserials['user']['name'] == TestUserUpdate.updated_user_data['name']

    @allure.title('Изменение данных: пользователь не зарегистрирован')
    def test_update_user_unauthenticated_expected_error(self):
        with allure.step('Отправляем запрос на изменение данных  пользователя, который не зарегистрирован, ожидаем ответ: код 401'):
            response = requests.patch(Urls.user_update, headers=Urls.headers, data=TestUserUpdate.updated_user_data)
        assert response.status_code == 401 and response.json() == negative_order_list