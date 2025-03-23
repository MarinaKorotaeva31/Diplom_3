from selenium.webdriver.common.by import By

class LocatorsOrdersFeedPage:
    # details_card = [By.CLASS_NAME, 'Modal_modal__container__Wo2l_']  # локатор карты заказа в ленте
    # локатор деталей в ленте заказов:
    details_card = [By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS']
    # надпись "В работе":
    in_work = [By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]']
    # счётчик "Выполнено за все время"
    done_all_time = [By.XPATH,
                     ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
    # счётчик "Выполнено за все сегодня"
    done_today = [By.XPATH,
                     ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
    # карта заказа в ленте заказов
    order = [By.XPATH, '//*[contains(@class,"OrderHistory_textBox__3lgbs mb-6")]']

