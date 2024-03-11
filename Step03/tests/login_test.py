import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as ChromeService
from pages import login_page


class TestLogin():

    @pytest.fixture
    def login(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver-win64', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert(login.success_message_present())

    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "bad password")
        assert(login.failure_message_present())        
