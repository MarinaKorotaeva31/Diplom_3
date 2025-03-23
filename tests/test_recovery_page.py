import allure
from data import Data
from tests.conftest import browser
from urls import Urls
from pages.account_page import AccountPage
from pages.password_recovery_page import RecoveryPasswordPage

class TestRecoveryPasswordPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Открывается страница входа в личный кабинет, листается до гиперссылки "Восстановить пароль",'
                        ' переход на страницу восстановления нажатием. Проверяется, что текущий урл соответствует'
                        ' странице восстановления пароля')
    def test_click_on_href_transfer_to_page_recovery_is_success(self, browser, open_account_page):
        account_page = AccountPage(browser)
        recovery_page = RecoveryPasswordPage(browser)
        account_page.wait_visibility_of_enter_button()
        account_page.scroll_to_recovery_password_href()
        account_page.click_on_recovery_password_button()
        recovery_page.wait_visibility_of_recovery_password_button()
        current_url = recovery_page.get_current_url()
        assert current_url == Urls.password_recovery


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Открывается страница восстановления пароля, в поле "Email" вводится почтовый адрес,'
                        ' клик по кнопке "Восстановить", проверка value и текущего урла')
    def test_input_email_is_success(self, browser, open_recovery_page):
        recovery_page = RecoveryPasswordPage(browser)
        recovery_page.wait_visibility_of_recovery_password_button()
        recovery_page.send_keys_to_input_email_field()
        value_field_email = recovery_page.get_field_email_value()
        recovery_page.click_on_recovery_password_button()
        recovery_page.wait_visibility_of_password_field()
        current_url = recovery_page.get_current_url()
        assert value_field_email == Data.EMAIL and current_url == Urls.password_recovery_page_2

    @allure.title('Проверяет, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Осуществляется переход на страницу восстановления, нажимается кнопка показать/скрыть пароль,'
                        ' проверяется видимость поля в активном состоянии')
    def test_click_and_activation_field(self, browser, open_recovery_page):
        recovery_page = RecoveryPasswordPage(browser)
        recovery_page.wait_visibility_of_recovery_password_button()
        recovery_page.click_on_recovery_password_button()
        recovery_page.wait_visibility_of_password_field()
        recovery_page.click_on_customization_button()
        assert recovery_page.wait_visibility_password_field_is_active()
