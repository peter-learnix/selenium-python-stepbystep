from selenium.webdriver.common.by import By
from . base_page import BasePage
from tests import config


class DynamicLoadingPage(BasePage):
    _start_button = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _finish_text = {"by": By.ID, "value": "finish"}

    def ___init___(self, driver):
        self.driver = driver

    def load_example(self, example_number, url = "/dynamic_loading/"):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url + example_number)
        self.driver.find_element(self._start_button['by'],
                                 self._start_button['value']).click()

    def finish_text_present(self):
        return self._is_displayed(self._finish_text, 10)
    