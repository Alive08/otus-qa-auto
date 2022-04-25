import os
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/webdrivers"))
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        browser = webdriver.Chrome(executable_path=f"{drivers}/chromedriver", options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        browser = webdriver.Firefox(executable_path=f"{drivers}/geckodriver", options=options)
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise ValueError("Browser not supported!")

    # browser.maximize_window()
    # request.addfinalizer(browser.close)

    yield browser

    browser.close()
    