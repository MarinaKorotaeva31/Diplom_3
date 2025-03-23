from pages.base_page import BasePage
from locators.locators_orders_feed_page import LocatorsOrdersFeedPage

class OrdersFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsOrdersFeedPage()
