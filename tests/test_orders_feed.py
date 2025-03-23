import allure
import pytest
import requests
import random
from urls import Urls
from pages.account_page import AccountPage
from pages.orders_feed_page import OrdersFeedPage
from locators.locators_account import LocatorsAccountPage
from locators.locators_base_page import LocatorsBasePage
from locators.locators_orders_feed_page import LocatorsOrdersFeedPage

class TestOrdersFeed:

    @allure.title('Проверка, что, если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Открывается страница ленты заказов, нажимается на первый заказ, находится'
                        ' крестик на окне деталей')
    def test_order_click_open_details(self, browser, open_orders_feed_page):
        browser_name = browser
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.wait_visibility_of_element(LocatorsOrdersFeedPage.order)
        orders_feed_page.click_on_element(LocatorsOrdersFeedPage.order, browser_name)
        assert orders_feed_page.find_of_element(LocatorsOrdersFeedPage.details_card)  # на


    @allure.title('Проверка, что заказы пользователя из «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создаётся аккаунт, осуществляется вход, создаётся заказ с помощью запроса, получается номер.'
                        ' Переход в историю заказов, получение номера последнего заказа. Переход в ленту заказов,'
                        ' получение номера заказа. Сравнение номеров заказов')
    def test_orders_from_history_displayed_in_orders_feed(self, browser, open_account_page, create_user_account):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        browser_name = browser
        access_token = create_user_account
        ingredients = {'ingredients': requests.get(Urls.get_ingredients).json()['data'][random.randint(0, 14)]['_id']}
        requests.post(Urls.create_orders, json=ingredients, headers={'Authorization': access_token})
        number_orders_current = requests.get(Urls.check_orders, headers={'Authorization': access_token}).json()['orders'][0]['number']

        account_page.login_to_account(browser_name)
        account_page.wait_clickable_element(LocatorsBasePage.h_order)
        orders_feed_page.click_on_element(LocatorsBasePage.button_account, browser_name)
        orders_feed_page.wait_visibility_of_element(LocatorsAccountPage.button_order_history)
        orders_feed_page.click_on_element(LocatorsAccountPage.button_order_history, browser_name)
        orders_feed_page.wait_visibility_of_element(LocatorsOrdersFeedPage.order)
        number_orders_history = orders_feed_page.find_of_element(LocatorsOrdersFeedPage.order).text.replace('\n', ' ').split(' ')
        number_orders_history = int(number_orders_history[0].replace('#', ''))

        orders_feed_page.click_on_element(LocatorsBasePage.button_feed, browser_name)
        orders_feed_page.wait_visibility_of_element(LocatorsOrdersFeedPage.done_all_time)
        number_orders_feed = orders_feed_page.find_of_element(LocatorsOrdersFeedPage.order).text.replace('\n', ' ').split(' ')
        number_orders_feed = int(number_orders_feed[0].replace('#', ''))

        assert number_orders_history == number_orders_current and number_orders_feed == number_orders_current

    @pytest.mark.parametrize(
        'locator, text',
        [
            (LocatorsOrdersFeedPage.done_all_time, 'за всё время'),
            (LocatorsOrdersFeedPage.done_today, 'за сегодня')
        ]
    )
    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено {text} увеличивается')
    @allure.description('Происходит создание аккаунта, авторизация. Переход к ленте заказов, считывание текущего'
                        ' количества заказов. Создается новый заказ через запрос, проверяется новое количество.'
                        ' Аккаунт удаляется')
    def test_add_new_order_increases_orders_count_all_time(self, browser, open_account_page, create_user_account, locator, text):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        browser_name = browser
        access_token = create_user_account
        orders_feed_page.wait_visibility_of_element(LocatorsAccountPage.input_email)
        account_page.login_to_account(browser_name)
        orders_feed_page.wait_visibility_of_element(LocatorsBasePage.h_order)
        orders_feed_page.click_on_element(LocatorsBasePage.button_feed, browser_name)
        orders_feed_page.wait_visibility_of_element(locator)
        num_orders = int(orders_feed_page.get_text(locator))

        ingredients = {'ingredients': requests.get(Urls.get_ingredients).json()['data'][random.randint(0, 14)]['_id']}
        requests.post(Urls.create_orders, json=ingredients, headers={'Authorization': access_token})
        new_num_orders = int(orders_feed_page.get_text(locator))

        assert new_num_orders == num_orders + 1


    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Происходит создание аккаунта, авторизация. Создается новый заказ через запрос, проверяется'
                        ' номер последнего заказа. С сайта в переменную сохраняется значение в разделе "В работе".'
                        ' Аккаунт удаляется')
    def test_new_order_visible_in_work(self, browser, open_account_page, create_user_account):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        browser_name = browser
        access_token = create_user_account
        orders_feed_page.wait_visibility_of_element(LocatorsAccountPage.input_email)
        account_page.login_to_account(browser_name)
        orders_feed_page.wait_visibility_of_element(LocatorsBasePage.h_order)
        orders_feed_page.click_on_element(LocatorsBasePage.button_feed, browser_name)

        ingredients = {'ingredients': requests.get(Urls.get_ingredients).json()['data'][random.randint(0, 14)]['_id']}
        requests.post(Urls.create_orders, json=ingredients, headers={'Authorization': access_token})
        number_orders_current = requests.get(Urls.check_orders, headers={'Authorization': access_token}).json()['orders'][0]['number']

        orders_feed_page.wait_visibility_of_element(LocatorsOrdersFeedPage.in_work)
        number_orders_on_site = int(orders_feed_page.get_text(LocatorsOrdersFeedPage.in_work))

        assert number_orders_current == number_orders_on_site
