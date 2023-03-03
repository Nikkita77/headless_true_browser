from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_add_todos():
    # browser.config.hold_browser_open = True

    chrome_options = Options()
    chrome_options.headless = True
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )


    browser.open('https://todomvc.com/examples/emberjs/')
