import allure
import pytest
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
#запускается, но
#selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home
@pytest.fixture(scope="session")
def browser_open_setting():
    browser.config.window_width = 1400 #NB!
    browser.config.window_height = 600
    yield
'''    

#def test_github(browser_open_setting):
def test_github():
    with allure.step("Open Home Page"):
        browser.open("https://github.com")
    with allure.step("Search"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("olgakos/demo_Dune_API")
    with allure.step("Submit"):
        s(".header-search-input").submit()
        s(by.link_text("olgakos/demo_Dune_API")).click()
    with allure.step("Check"):
        s("#issues-tab").click()
        s(by.partial_text("#1")).should(be.visible)
