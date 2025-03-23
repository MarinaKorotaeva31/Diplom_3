import allure
import pytest
from api_methods import ApiMethods
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.orders_feed_page import OrdersFeedPage
from locators.locators_orders_feed_page import LocatorsOrdersFeedPage

class TestOrdersFeed:

    @allure.title('Проверка, что, если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Открывается страница ленты заказов, нажимается на первый заказ, находится'
                        ' крестик на окне деталей')
    def test_order_click_open_details(self, browser, open_orders_feed_page):
        orders_feed_page = OrdersFeedPage(browser)
        orders_feed_page.wait_visibility_order_card()
        orders_feed_page.click_on_order_card()
        assert orders_feed_page.found_close_details()


    @allure.title('Проверка, что заказы пользователя из «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создаётся аккаунт, осуществляется вход, создаётся заказ с помощью запроса, получается номер.'
                        ' Переход в историю заказов, получение номера последнего заказа. Переход в ленту заказов,'
                        ' получение номера заказа. Сравнение номеров заказов')
    def test_orders_from_history_displayed_in_orders_feed(self, browser, open_account_page, create_user_account):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        main_page = MainPage(browser)
        access_token = create_user_account
        api_method = ApiMethods()
        api_method.create_orders(access_token)
        number_orders_current = api_method.get_order_number(create_user_account)

        account_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_login_button()
        account_page.wait_clickable_orders_history()
        account_page.click_on_orders_history()
        orders_feed_page.wait_visibility_order_card()
        number_orders_history = orders_feed_page.find_order_card()

        main_page.click_on_orders_feed()
        orders_feed_page.wait_visibility_text_all_time()
        number_orders_feed = orders_feed_page.find_order_card()

        assert number_orders_history == number_orders_current and number_orders_feed == number_orders_current


    # локаторы в тесте оставлены для параметризации
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
    def test_add_new_order_increases_orders_count(self, create_user_account, browser, open_account_page, locator, text):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        main_page = MainPage(browser)

        access_token = create_user_account

        account_page.wait_visibility_of_email_field()
        account_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_orders_feed()
        orders_feed_page.wait_visibility_of_element(locator)
        num_orders = int(orders_feed_page.get_text(locator))

        api_method = ApiMethods()
        api_method.create_orders(access_token)
        new_num_orders = int(orders_feed_page.get_text(locator))

        assert new_num_orders == num_orders + 1


    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Происходит создание аккаунта, авторизация. Создается новый заказ через запрос, проверяется'
                        ' номер последнего заказа. С сайта в переменную сохраняется значение в разделе "В работе".'
                        ' Аккаунт удаляется')
    def test_new_order_visible_in_work(self, browser, open_account_page, create_user_account):
        orders_feed_page = OrdersFeedPage(browser)
        account_page = AccountPage(browser)
        main_page = MainPage(browser)

        access_token = create_user_account

        account_page.wait_visibility_of_email_field()
        account_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_orders_feed()

        api_method = ApiMethods()
        api_method.create_orders(access_token)
        number_orders_current = api_method.get_order_number(create_user_account)

        orders_feed_page.wait_visibility_in_work()
        number_orders_on_site = orders_feed_page.text_order_number_in_work()

        assert number_orders_current == number_orders_on_site
