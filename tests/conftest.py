import pytest
import allure
import requests
from data import Data
from urls import Urls
from webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser to run tests on')

@allure.step('Создание и закрытие браузера')
@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    driver = WebdriverFactory.get_webdriver(browser_name)
    yield driver
    driver.quit()

@allure.step('Открываем главную страницу')
@pytest.fixture
def open_main_page(browser):
    browser.get(Urls.main_page)
    browser.maximize_window()

@allure.step('Открываем страницу личного кабинета')
@pytest.fixture
def open_account_page(browser):
    browser.get(Urls.account)
    browser.maximize_window()

@allure.step('Открываем страницу восстановления пароля')
@pytest.fixture
def open_recovery_page(browser):
    browser.get(Urls.password_recovery)
    browser.maximize_window()


@allure.step('Открываем страницу ленты заказов')
@pytest.fixture
def open_orders_feed_page(browser):
    browser.get(Urls.feed_page)
    browser.maximize_window()

@pytest.fixture
def create_user_account():
    response = requests.post(url=Urls.create_user, json={"email": Data.EMAIL, "password": Data.PASSWORD, "name": Data.NAME})
    access_token = response.json().get('accessToken')
    yield access_token
    requests.delete(Urls.delete_user, headers={'Authorization': access_token})
