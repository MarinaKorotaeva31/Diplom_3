import allure
from pages.base_page import BasePage
from locators.locators_orders_feed_page import LocatorsOrdersFeedPage

class OrdersFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsOrdersFeedPage()

    @allure.step('Ожидание видимости карты заказа')
    def wait_visibility_order_card(self):
        return self.wait_visibility_of_element(LocatorsOrdersFeedPage.order)

    @allure.step('Ожидание видимости надписи "Выполнено за все время"')
    def wait_visibility_text_all_time(self):
        return self.wait_visibility_of_element(LocatorsOrdersFeedPage.done_all_time)

    @allure.step('Ожидание видимости надписи "В работе"')
    def wait_visibility_in_work(self):
        return self.wait_visibility_of_element(LocatorsOrdersFeedPage.in_work)

    @allure.step('Получение номер заказа под надписью "В работе"')
    def text_order_number_in_work(self):
        return int(self.get_text(LocatorsOrdersFeedPage.in_work))

    @allure.step('Поиск номера карты заказа')
    def find_order_card(self):
        num = self.find_of_element(LocatorsOrdersFeedPage.order).text.replace('\n', ' ').split(' ')
        return int(num[0].replace('#', ''))

    @allure.step('Поиск кнопки закрытия карты заказа')
    def found_close_details(self):
        return self.find_of_element(LocatorsOrdersFeedPage.details_card)

    @allure.step('Нажатие на карту заказа')
    def click_on_order_card(self):
        return self.click_on_element(LocatorsOrdersFeedPage.order, self.browser)
