from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    def __init__(self, locator: tuple, driver: object):
        self.locator = locator
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def get_element(self) -> object:
        self.wait.until(lambda driver: driver.find_element(*self.locator))
        element = self.driver.find_element(*self.locator)
        return element

    def get_elements(self) -> list:
        self.wait.until(lambda driver: driver.find_elements(*self.locator))
        elements = self.driver.find_elements(*self.locator)
        return elements


class SearchTextPageElement(BasePageElement):

    def set_value(self, value: str) -> None:
        self.wait.until(lambda driver: driver.find_element(*self.locator))
        self.driver.find_element(*self.locator).send_keys(value)

    def get_value(self) -> str:
        self.wait.until(lambda driver: driver.find_element(*self.locator))
        element = self.driver.find_element(*self.locator)
        return element.get_attribute("value")
