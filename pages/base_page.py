import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.action = ActionChains(browser)

    @allure.step('Ищем элемент "{locator}" на странице')
    def find_of_element(self, locator):
        return self.browser.find_element(*locator)

    @allure.step('Нажимаем на элемент "{locator}"')
    def click_on_element(self, locator, browser_name):
        if 'chrome' in str(browser_name):
            self.browser.find_element(*locator).click()
        elif 'firefox' in str(browser_name):
            element = self.browser.find_element(*locator)
            return  self.browser.execute_script("arguments[0].click();", element)

    @allure.step('Заполняем поле ввода "{locator}": {keys}')
    def send_keys_to_input(self, locator, keys):
        return self.browser.find_element(*locator).send_keys(keys)

    @allure.step('Листаем до элемента "{locator}"')
    def scrolling_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем появления элемента "{locator}" на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем становление элемента "{locator}" кликабельным на странице')
    def wait_clickable_element(self, locator):
        return WebDriverWait(self.browser, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидаем исчезновение элемента "{locator}" на странице')
    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.browser, 5).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Получаем текст элемента "{locator}"')
    def get_text(self, locator):
        return self.browser.find_element(*locator).text

    @allure.step('Получаем атрибут элемента "{locator}"')
    def get_attribute(self, locator):
        return self.browser.find_element(*locator).get_attribute("value")

    @allure.step('Получаем текущий url')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Перетаскивание ингредиента')
    def drag_and_drop_ingredients(self, element_1, element_2):
        self.action.drag_and_drop(element_1, element_2)
        self.action.perform()

    @allure.step('Drag-and-drop элемента')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(source_locator))
        target_element = WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(target_locator))

        # JavaScript для перетаскивания
        self.browser.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
        )
