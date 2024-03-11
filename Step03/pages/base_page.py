from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    

    def _is_displayed(self, locator):
        try:
            return self.driver.find_element(locator['by'], locator['value'])
        except NoSuchElementException:
            return False