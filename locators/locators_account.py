from selenium.webdriver.common.by import By

class LocatorsAccountPage:
    href_recovery_password = [By.XPATH, './/a[@href="/forgot-password"]']  # гиперссылка "Восстановить пароль"
    button_enter = [By.XPATH, './/button[text() = "Войти"]']  # кнопка "Войти"
    button_exit = [By.XPATH, './/button[text() = "Выход"]']  # кнопка "Выход" в личном кабинете
    button_order_history = [By.XPATH, './/a[@href="/account/order-history"]']  # кнопка "История заказов"
    input_email = [By.NAME, "name"]  # поле ввода Email
    input_password = [By.NAME, 'Пароль']  # поле ввода Пароля

