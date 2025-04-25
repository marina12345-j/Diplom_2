import allure
import pytest
import requests
from data import *
from urls import Urls


class TestCreateOrder:
    @allure.title('Проверка ответа о создании заказа с успешной авторизацией пользователя и '
                  'с указанными ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_authenticated_user(self, new_user_creature_and_delete, burger_ingredients):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': [burger_ingredients]}
        with allure.step('Отправляем запрос на создание заказа с валидными ингредиентами, '
                         'пользователь успешно авторизован, ожидаем ответ: код 200, в теле ответа наименование ингредиента'
                         'номер заказа'):
            response = requests.post(Urls.order_create, data=payload, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'name' in deserials.keys()
        assert 'number' in deserials['order'].keys()

    @allure.title('Проверка ответа о создании заказа и с указанными ингредиентами без авторизации пользователя'
                 'с помощью фикстуры создается два заказа с разными ингредиентами.')
    @allure.issue('Заказ создается неавторизованным пользователем, код ответа 200')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_unauthenticated_user_success(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        with allure.step('Отправляем запрос на создание заказа с валидными ингредиентами, '
                         'пользователь не авторизован, ожидаем ответ: код 403'):
            response = requests.post(Urls.order_create, data=payload)
        assert response.status_code == 403 and response.json() == CreateOrder.user_not_logged

    @allure.title('Проверка ответа о создании заказа с успешной авторизацией пользователя и без ингредиентов')
    def test_create_order_empty_ingredients_authenticated_user_expected_error(self, new_user_creature_and_delete):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        with allure.step('Отправляем запрос на создание заказа без ингредиентов, '
                         'пользователь успешно авторизован, ожидаем ответ: код 400'):
            response = requests.post(Urls.order_create, data=payload, headers=headers)
        assert response.status_code == 400 and response.json() == CreateOrder.ingredient_must_be_provided

    @allure.title('Проверка ответа о создании заказа с успешной авторизацией пользователя и с неверным хэшем ингредиентов'
                  'аутентифицированным юзером')
    def test_create_order_invalid_ingredients_authenticated_user_expected_error(self, new_user_creature_and_delete):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash_ingredient]}
        with allure.step('Отправляем запрос на создание заказа  ингредиентов с неверным хэшем ингредиентов, '
                         'пользователь успешно авторизован, ожидаем ответ: код 500'):
            response = requests.post(Urls.order_create, data=payload, headers=headers)
        assert response.status_code == 500


