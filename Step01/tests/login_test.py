import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as ChromeService


class TestLogin():

    @pytest.fixture
    def driver(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver-win64', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys(
            "SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        assert(
            driver.find_element(
                By.CSS_SELECTOR,
                ".flash.success").is_displayed())
        #assert(driver.find_element(By.CSS_SELECTOR, ".flash.success").is_displayed())