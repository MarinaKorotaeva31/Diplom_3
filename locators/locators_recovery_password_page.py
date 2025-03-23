from selenium.webdriver.common.by import By

class LocatorsRecoveryPasswordPage:
    button_recovery = [By.XPATH, './/button[text() = "Восстановить"]']  # кнопка "Восстановить"
    input_email = [By.NAME, "name"]  # поле ввода Email
    input_password = [By.NAME, 'Введите новый пароль']  # поле ввода Пароля
    check_click = [By.CSS_SELECTOR, '.input__icon-action']  # кнопка скрытия/показа пароля
    check_active = [By.CSS_SELECTOR, '.input_status_active']  # поле ввода пароля в активном состоянии
