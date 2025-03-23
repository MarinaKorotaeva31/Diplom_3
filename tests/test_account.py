import allure
from urls import Urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from locators.locators_account import LocatorsAccountPage

class TestAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Проверяется переход с главной страницы на страницу входа в аккаунт по нажатию кнопки'
                        ' "Личный кабинет", по окончании теста проверяется урл страницы личного кабинета')
    def test_click_button_account_transfer_to_account(self, browser, open_main_page):
        main_page = MainPage(browser)
        account_page = AccountPage(browser)
        main_page.wait_clickable_login_button()
        main_page.click_on_login_button()
        account_page.wait_clickable_enter_button()
        current_utl = account_page.get_current_url()
        assert current_utl == Urls.account


    @allure.title('Проверяется переход в раздел «История заказов»')
    @allure.description('Осуществляется регистрация и вход в аккаунт, далее переход в личный кабинет, нажатие кнопки "История заказов"'
                        ' проверка текущего урла - урл страницы истории заказов. Для хрома и firefox используются разные методы'
                        ' клика по кнопке "Личный кабинет"')
    def test_transfer_to_order_history(self, create_user_account, browser, open_account_page):
        account_page = AccountPage(browser)
        main_page = MainPage(browser)
        account_page.wait_visibility_of_email_field()
        account_page.login_to_account()
        main_page.wait_clickable_order_button()  # ожидание загрузки главной страницы
        main_page.click_on_login_button()
        account_page.wait_clickable_orders_history()
        account_page.click_on_orders_history()
        current_url = account_page.get_current_url()
        assert current_url == Urls.order_history

    @allure.title('Проверка выхода из аккаунта')
    @allure.description(
        'Осуществляется регистрация и вход в аккаунт, далее переход в личный кабинет, нажатие кнопки "Выход"'
        ' проверка текущего урла - урл страницы входа. Для хрома и firefox используются разные методы'
        ' клика по кнопке "Личный кабинет"')
    def test_exit_from_account_is_success(self, create_user_account, browser, open_account_page):
        account_page = AccountPage(browser)
        main_page = MainPage(browser)
        account_page.wait_visibility_of_email_field()
        account_page.login_to_account()
        main_page.wait_clickable_order_button()  # ожидание загрузки главной страницы
        # (кнопки оформить заказ) для прохода теста в firefox
        main_page.click_on_login_button()
        account_page.wait_visibility_of_element(LocatorsAccountPage.button_exit)
        account_page.click_on_exit_button()
        account_page.wait_visibility_of_enter_button()
        current_url = account_page.get_current_url()
        assert current_url == Urls.account
