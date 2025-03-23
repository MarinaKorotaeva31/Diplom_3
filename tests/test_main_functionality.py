import allure
from urls import Urls
from pages.account_page import AccountPage
from pages.main_page import MainPage

class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Осуществляется переход в личный кабинет, нажимается кнопка "Конструктор",'
                        ' проверяется урл текущей страницы == урл главной страницы')
    def test_transfer_to_constructor_is_success(self, browser, open_account_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_constructor_button()
        main_page.click_on_constructor_button()
        main_page.wait_clickable_enter_button()
        assert browser.current_url == Urls.main_page


    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Осуществляется переход в личный кабинет, нажимается кнопка "Лента заказов",'
                        ' проверяется урл текущей страницы == урл главной страницы')
    def test_transfer_to_order_feed_is_success(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_orders_feed()
        main_page.click_on_orders_feed()
        main_page.wait_invisibility_order_button()
        assert browser.current_url == Urls.feed_page


    @allure.title('Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Осуществляется переход на главную страницу, нажимается кнопка "Флюоресцентная булка R2-D3",'
                        ' проверяется видимость страницы с деталями об ингредиенте')
    def test_click_ingredient_call_details(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_ingredient()
        main_page.click_on_ingredient_card()
        assert main_page.wait_visibility_ingredients_card()


    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    @allure.description('Осуществляется переход на главную страницу, нажимается кнопка "Флюоресцентная булка R2-D3",'
                        ' проверяется кликабельность "крестика", нажимается "крестик", проверяется видимость'
                        ' надписи "Соберите бургер"')
    def test_click_button_close_details_window_is_success(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_ingredient()
        main_page.click_on_ingredient_card()
        main_page.wait_clickable_close_symbol()
        main_page.click_close_symbol()
        assert main_page.wait_clickable_enter_button()


    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Осуществляется переход на главную страницу, считывается текущий каунтер, перетаскивается'
                        ' флюоресцентная булка, проверяется увеличение каунтера на 2')
    def test_add_ingredient_increases_counter(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_enter_button()
        count_start = int(main_page.get_text_count_ingredient_in_order())
        main_page.drag_and_drop_ingredients()
        count_end = int(main_page.get_text_count_ingredient_in_order())
        assert count_end == count_start + 2


    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description(
        'Осуществляется регистрация и вход в аккаунт, далее нажимается кнопка "Оформить заказ", проверяется'
        ' текст в открытом окне. Для хрома и firefox используются разные методы клика по кнопке "Личный кабинет"')
    def test_order_authorized_is_success(self, browser, open_account_page, create_user_account):
        main_page = MainPage(browser)
        account_page = AccountPage(browser)
        account_page.wait_visibility_of_email_field()
        account_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_order_button()
        assert main_page.wait_visibility_orders_window()
