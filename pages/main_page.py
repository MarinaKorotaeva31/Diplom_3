import allure
from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsMainPage()

    @allure.step('Ожидание кликабельности кнопки "Личный кабинет"')
    def wait_clickable_login_button(self):
        return self.wait_clickable_element(LocatorsMainPage.button_account)

    @allure.step('Ожидание кликабельности кнопки "Оформить заказ"')
    def wait_clickable_order_button(self):
        return self.wait_clickable_element(LocatorsMainPage.button_order)

    @allure.step('Ожидание кликабельности кнопки "Войти в аккаунт"')
    def wait_clickable_enter_button(self):
        return self.wait_clickable_element(LocatorsMainPage.button_log_in_to_account)

    @allure.step('Ожидание кликабельности кнопки "Конструктор"')
    def wait_clickable_constructor_button(self):
        return self.wait_clickable_element(LocatorsMainPage.button_constructor)

    @allure.step('Ожидание кликабельности кнопки "Лента Заказов"')
    def wait_clickable_orders_feed(self):
        return self.wait_clickable_element(LocatorsMainPage.button_feed)

    @allure.step('Ожидание кликабельности кнопки "Крестик" в деталях ингредиента')
    def wait_clickable_close_symbol(self):
        return self.wait_clickable_element(LocatorsMainPage.button_close_details)

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_on_login_button(self):
        return self.click_on_element(LocatorsMainPage.button_account, self.browser)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        return self.click_on_element(LocatorsMainPage.button_order, self.browser)

    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        return self.click_on_element(LocatorsMainPage.button_constructor, self.browser)

    @allure.step('Нажатие на кнопку "Лента Заказов"')
    def click_on_orders_feed(self):
        return self.click_on_element(LocatorsMainPage.button_feed, self.browser)

    @allure.step('Нажатие на карточку ингредиента')
    def click_on_ingredient_card(self):
        return self.click_on_element(LocatorsMainPage.button_ingredient_bun, self.browser)

    @allure.step('Нажатие на кнопку "Крестик" в деталях ингредиента')
    def click_close_symbol(self):
        return self.click_on_element(LocatorsMainPage.button_close_details, self.browser)

    @allure.step('Ожидание невидимости надписи "Соберите бургер"')
    def wait_invisibility_order_button(self):
        return self.wait_invisibility_of_element(LocatorsMainPage.h_order)

    @allure.step('Ожидание кликабельности кнопки ингредиента')
    def wait_clickable_ingredient(self):
        return self.wait_clickable_element(LocatorsMainPage.button_ingredient_bun)

    @allure.step('Ожидание видимости деталей ингредиента')
    def wait_visibility_ingredients_card(self):
        return self.wait_visibility_of_element(LocatorsMainPage.h_ingredient)

    @allure.step('Ожидание видимости окна заказа')
    def wait_visibility_orders_window(self):
        return self.wait_visibility_of_element(LocatorsMainPage.text_order)

    @allure.step('Получение каунтера ингредиента')
    def get_text_count_ingredient_in_order(self):
        return self.get_text(LocatorsMainPage.bun_counter)
