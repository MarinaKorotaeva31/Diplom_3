import allure
from data import Data
from pages.base_page import BasePage
from locators.locators_account import LocatorsAccountPage


class AccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsAccountPage()

    @allure.step('Ожидание кликабельности кнопки "Войти"')
    def wait_clickable_enter_button(self):
        return self.wait_clickable_element(LocatorsAccountPage.button_enter)

    @allure.step('Ожидание кликабельности кнопки "История заказов"')
    def wait_clickable_orders_history(self):
        return self.wait_clickable_element(LocatorsAccountPage.button_order_history)

    @allure.step('Ожидание видимости поля "Email"')
    def wait_visibility_of_email_field(self):
        return self.wait_clickable_element(LocatorsAccountPage.input_email)

    @allure.step('Ожидание видимости кнопки "Войти"')
    def wait_visibility_of_enter_button(self):
        return self.wait_visibility_of_element(LocatorsAccountPage.button_enter)

    @allure.step('Нажатие на кнопку "История заказов"')
    def click_on_orders_history(self):
        return self.click_on_element(LocatorsAccountPage.button_order_history, self.browser)

    @allure.step('Нажатие на кнопку "Выход"')
    def click_on_exit_button(self):
        return self.click_on_element(LocatorsAccountPage.button_exit, self.browser)

    @allure.step('Ожидание видимости кнопки "Выход"')
    def wait_visibility_exit_button(self):
        return self.wait_visibility_of_element(LocatorsAccountPage.button_exit)

    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def click_on_recovery_password_button(self):
        return self.click_on_element(LocatorsAccountPage.href_recovery_password, self.browser)

    @allure.step('Прокручивание страницы до кнопки "Восстановить пароль"')
    def scroll_to_recovery_password_href(self):
        return self.scrolling_to_element(LocatorsAccountPage.href_recovery_password)

    @allure.step('Вход в аккаунт')
    def login_to_account(self):
        self.send_keys_to_input(LocatorsAccountPage.input_email, Data.EMAIL)
        self.send_keys_to_input(LocatorsAccountPage.input_password, Data.PASSWORD)
        self.click_on_element(LocatorsAccountPage.button_enter, self.browser)
