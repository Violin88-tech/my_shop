import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv

from my_shop_project_test.utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://my-shop.ru'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

# import pytest
# from selene import browser
# from selenium import webdriver
#
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_management():
#     browser.config.base_url = 'https://my-shop.ru'
#     driver_options = webdriver.ChromeOptions()
#     # driver_options.add_argument('--headless')
#     browser.config.driver_options = driver_options
#
#     # browser.config.timeout = 4
#
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#     yield
#
#     browser.quit()
