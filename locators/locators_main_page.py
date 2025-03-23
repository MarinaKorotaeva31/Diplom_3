from selenium.webdriver.common.by import By

class LocatorsMainPage:
    button_account = [By.XPATH, './/a[@href="/account"]']  # кнопка "Личный кабинет"
    button_constructor = [By.XPATH, './/p[text()="Конструктор"]']  # кнопка "Конструктор"
    button_feed = [By.XPATH, './/a[@href="/feed"]']  # кнопка "Лента заказов"
    button_ingredient_bun = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]']  # ингредиент булка
    button_close_details = [By.CSS_SELECTOR, '.Modal_modal__close__TnseK']  # крестик для закрытия деталей ингредиента
    button_order = (By.XPATH, './/button[text() = "Оформить заказ"]')  # кнопка "Оформить заказ"
    button_log_in_to_account = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"

    h_order = [By.XPATH, './/h1[text() = "Соберите бургер"]']  # заголовок "Соберите бургер"
    h_ingredient = [By.XPATH, './/h2[text() = "Детали ингредиента"]']  # детали ингредиента
    order_feed_text = [By.XPATH, './/h1[text() = "Лента заказов"]']  # заголовок "Лента заказов"
    from_element = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]']  # локатор булки для перетаскивания
    bun_counter = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//div[@class="counter_counter__ZNLkj counter_default__28sqi"]']
    text_order = [By.XPATH, './/p[text()="Ваш заказ начали готовить"]']  # надпись при оформлении заказа
    field_for_add_to_order = [By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7']  # место добавления заказа
