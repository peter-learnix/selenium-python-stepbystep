import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from . import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://the-internet.herokuapp.com",
                     help="base URL for the application under test")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")

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