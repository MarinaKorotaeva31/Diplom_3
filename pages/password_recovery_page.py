import allure
from data import Data
from pages.base_page import BasePage
from locators.locators_recovery_password_page import LocatorsRecoveryPasswordPage

class RecoveryPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsRecoveryPasswordPage()

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_recovery_password_button(self):
        return self.click_on_element(LocatorsRecoveryPasswordPage.button_recovery, self.browser)

    @allure.step('Нажатие на кнопку "Скрыть/показать пароль"')
    def click_on_customization_button(self):
        return self.click_on_element(LocatorsRecoveryPasswordPage.check_click, self.browser)

    @allure.step('Ожидание видимости кнопки "Восстановить пароль"')
    def wait_visibility_of_recovery_password_button(self):
        return self.wait_visibility_of_element(LocatorsRecoveryPasswordPage.button_recovery)

    @allure.step('Ожидание активации поля "Пароль"')
    def wait_visibility_password_field_is_active(self):
        return self.wait_visibility_of_element(LocatorsRecoveryPasswordPage.check_active)

    @allure.step('Заполнение поля "Email"')
    def send_keys_to_input_email_field(self):
        return self.send_keys_to_input(LocatorsRecoveryPasswordPage.input_email, Data.EMAIL)

    @allure.step('Получение значения из поля "Email"')
    def get_field_email_value(self):
        return self.get_attribute(LocatorsRecoveryPasswordPage.input_email)

    @allure.step('Ожидание видимости поля "Пароль"')
    def wait_visibility_of_password_field(self):
        return self.wait_clickable_element(LocatorsRecoveryPasswordPage.input_password)
