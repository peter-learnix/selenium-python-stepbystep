import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as ChromeService
from pages import dynamic_loading_page


class TestDynamicLoading():

    @pytest.fixture
    def dynamic_loading(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver-win64', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return dynamic_loading_page.DynamicLoadingPage(driver_)
    
    def test_hidden_element(self, dynamic_loading):
        dynamic_loading.load_example("1")
        assert(dynamic_loading.finish_text_present())

    def test_rendered_element(self, dynamic_loading):
        dynamic_loading.load_example("2")
        assert(dynamic_loading.finish_text_present())