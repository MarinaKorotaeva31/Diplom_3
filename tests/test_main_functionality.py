import allure
from urls import Urls
from pages.base_page import BasePage
from pages.account_page import AccountPage
from locators.locators_base_page import LocatorsBasePage
from locators.locators_account import LocatorsAccountPage

class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Осуществляется переход в личный кабинет, нажимается кнопка "Конструктор",'
                        ' проверяется урл текущей страницы == урл главной страницы')
    def test_transfer_to_constructor_is_success(self, browser, open_account_page):
        browser_name = browser
        main_page = BasePage(browser)
        main_page.wait_clickable_element(LocatorsBasePage.button_constructor)
        main_page.click_on_element(LocatorsBasePage.button_constructor, browser_name)
        main_page.wait_visibility_of_element(LocatorsBasePage.h_order)
        assert browser.current_url == Urls.main_page

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Осуществляется переход в личный кабинет, нажимается кнопка "Лента заказов",'
                        ' проверяется урл текущей страницы == урл главной страницы')
    def test_transfer_to_order_feed_is_success(self, browser, open_main_page):
        browser_name = browser
        main_page = BasePage(browser)
        main_page.wait_clickable_element(LocatorsBasePage.button_feed)
        main_page.click_on_element(LocatorsBasePage.button_feed, browser_name)
        main_page.wait_invisibility_of_element(LocatorsBasePage.h_order)
        assert browser.current_url == Urls.feed_page


    @allure.title('Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Осуществляется переход на главную страницу, нажимается кнопка "Флюоресцентная булка R2-D3",'
                        ' проверяется видимость страницы с деталями об ингредиенте')
    def test_click_ingredient_call_details(self, browser, open_main_page):
        browser_name = browser
        main_page = BasePage(browser)
        main_page.wait_clickable_element(LocatorsBasePage.button_ingredient_bun)
        main_page.click_on_element(LocatorsBasePage.button_ingredient_bun, browser_name)
        main_page.wait_visibility_of_element(LocatorsBasePage.h_ingredient)
        assert main_page.wait_visibility_of_element(LocatorsBasePage.h_ingredient)

    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    @allure.description('Осуществляется переход на главную страницу, нажимается кнопка "Флюоресцентная булка R2-D3",'
                        ' проверяется кликабельность "крестика", нажимается "крестик", проверяется видимость'
                        ' надписи "Соберите бургер"')
    def test_click_button_close_details_window_is_success(self, browser, open_main_page):
        browser_name = browser
        main_page = BasePage(browser)
        main_page.wait_clickable_element(LocatorsBasePage.button_ingredient_bun)
        main_page.click_on_element(LocatorsBasePage.button_ingredient_bun, browser_name)
        main_page.wait_clickable_element(LocatorsBasePage.button_close_details)
        main_page.click_on_element(LocatorsBasePage.button_close_details, browser_name)
        assert main_page.wait_visibility_of_element(LocatorsBasePage.h_order)


    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Осуществляется переход на главную страницу, считывается текущий каунтер, перетаскивается'
                        ' флюоресцентная булка, проверяется увеличение каунтера на 2')
    def test_add_ingredient_increases_counter(self, browser, open_main_page):
        main_page = BasePage(browser)
        browser_name = browser
        main_page.wait_clickable_element(LocatorsBasePage.button_log_in_to_account)
        count_start = int(main_page.get_text(LocatorsBasePage.bun_counter))
        from_element = main_page.find_of_element(LocatorsBasePage.from_element)
        to_element = main_page.find_of_element(LocatorsBasePage.field_for_add_to_order)
        if 'chrome' in str(browser_name):
            main_page.drag_and_drop_ingredients(from_element, to_element)
        elif 'firefox' in str(browser_name):
            main_page.drag_and_drop_element(LocatorsBasePage.from_element, LocatorsBasePage.field_for_add_to_order)
        count_end = int(main_page.get_text(LocatorsBasePage.bun_counter))
        assert count_end == count_start + 2


    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description(
        'Осуществляется регистрация и вход в аккаунт, далее нажимается кнопка "Оформить заказ", проверяется'
        ' текст в открытом окне. Для хрома и firefox используются разные методы клика по кнопке "Личный кабинет"')
    def test_order_authorized_is_success(self, browser, open_account_page, create_user_account):
        main_page = BasePage(browser)
        account_page = AccountPage(browser)
        browser_name = browser
        main_page.wait_visibility_of_element(LocatorsAccountPage.input_email)
        account_page.login_to_account(browser_name)
        main_page.wait_clickable_element(LocatorsBasePage.button_order)
        main_page.click_on_element(LocatorsBasePage.button_order, browser_name)
        assert main_page.wait_visibility_of_element(LocatorsBasePage.text_order)
