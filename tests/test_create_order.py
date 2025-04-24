import allure
import pytest
import requests
from data import IngredientData
from urls import Urls


class TestCreateOrder:
    @allure.title('Проверка ответа о создании заказа')
    @allure.step('Проверка ответа о создании заказа с успешной авторизацией пользователя и с указанными ингредиентами'
                        'с помощью фикстуры создается два заказа с разными ингредиентами.')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_authenticated_user(self, new_user_creature_and_delete, burger_ingredients):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Urls.order_create, data=payload, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'name' in deserials.keys()
        assert 'number' in deserials['order'].keys()

    @allure.step('Проверка ответа о создании заказа и с указанными ингредиентами без авторизации пользователя'
                 'с помощью фикстуры создается два заказа с разными ингредиентами.')
    @allure.issue('Заказ создается неавторизованным пользователем')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_unauthenticated_user_success(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Urls.order_create, data=payload)
        assert response.status_code == 403 and response.json() == {'success': False,
                                                                  'message': 'Email, password and name are required fields'}

    @allure.step('Проверка ответа о создании заказа с успешной авторизацией пользователя и без ингредиентов')
    def test_create_order_empty_ingredients_authenticated_user_expected_error(self, new_user_creature_and_delete):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Urls.order_create, data=payload, headers=headers)
        assert response.status_code == 400 and response.json() == {'success': False,
                                                                   'message': 'Ingredient ids must be provided'}

    @allure.step('Проверка ответа о создании заказа с успешной авторизацией пользователя и с неверным хэшем ингредиентов'
                  'аутентифицированным юзером')
    def test_create_order_invalid_ingredients_authenticated_user_expected_error(self, new_user_creature_and_delete):
        headers = {'Authorization': new_user_creature_and_delete[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash_ingredient]}
        response = requests.post(Urls.order_create, data=payload, headers=headers)
        assert response.status_code == 500 and "Internal Server Error" in response.text


