import allure
from data import Data
from pages.base_page import BasePage
from locators.locators_account import LocatorsAccountPage


class AccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsAccountPage()

    @allure.step('Вход в аккаунт')
    def login_to_account(self, browser_name):
        self.send_keys_to_input(LocatorsAccountPage.input_email, Data.EMAIL)
        self.send_keys_to_input(LocatorsAccountPage.input_password, Data.PASSWORD)
        self.click_on_element(LocatorsAccountPage.button_enter, browser_name)
