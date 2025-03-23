import requests
import allure
import random
from data import Data
from urls import Urls

class ApiMethods:
    @allure.step('Создание пользователя')
    def create_account(self):
        response = requests.post(url=Urls.create_user, json={"email": Data.EMAIL, "password": Data.PASSWORD,
                                                             "name": Data.NAME})
        return response

    @allure.step('Получение токена для авторизации')
    def get_access_token(self):
        response = self.create_account()
        access_token = response.json().get('accessToken')
        return access_token

    @allure.step('Создание заказа')
    def create_orders(self, access_token: str):
        response = requests.get(Urls.get_ingredients)
        ingredients_data = response.json()['data']
        ingredients = {'ingredients': ingredients_data[random.randint(0, len(ingredients_data) - 1)]['_id']}
        return requests.post(Urls.create_orders, json=ingredients, headers={'Authorization': access_token})

    @allure.step('Получение номера заказа')
    def get_order_number(self, access_token):
        response = requests.get(Urls.check_orders, headers={'Authorization': access_token})
        return response.json()['orders'][0]['number']
