import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    browser.config.driver_options = driver_options
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.base_url = 'https://github.com'
    yield

    browser.quit()