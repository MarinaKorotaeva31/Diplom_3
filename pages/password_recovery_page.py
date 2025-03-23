from locators.locators_recovery_password_page import LocatorsRecoveryPasswordPage
from pages.base_page import BasePage

class RecoveryPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsRecoveryPasswordPage()
