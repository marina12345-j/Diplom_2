import allure
import requests

from data import *
from urls import Urls

class TestGetOrders:
    @allure.title('Проверка получения списка заказов')
    @allure.step('Проверка успешного получения списка заказов для авторизованного пользователя')
    def test_get_orders_authenticated_user_success(self, create_user_and_order_and_delete):
        headers = {'Authorization': create_user_and_order_and_delete[0]}
        with allure.step('Отправляем запрос на получение списка заказов, пользователь '
                         'успешно авторизован, ожидаем ответ: код 200, в теле хеш ингредиентов, номер заказа, статус заказа'):
            response = requests.get(Urls.get_user_orders, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'orders' in deserials.keys()
        assert 'total' in deserials.keys()

    @allure.title('Проверка успешного получения списка заказов для неавторизованного пользователя')
    def test_get_orders_unauthenticated_user_success(self):
        with allure.step('Отправляем запрос на получение списка заказов, пользователь не авторизован,'
                         'ожидаем ответ: код 401'):
            response = requests.get(Urls.get_user_orders, headers=Urls.headers)
        assert response.status_code == 401 and response.json() == negative_order_list