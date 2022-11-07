import allure
import pytest
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
@pytest.fixture(scope="session")
def browser_open_setting(): #?(setup_browser)
    browser.config.window_width = 1400 #размер окна важен 
    browser.config.window_height = 600 #размер окна важен 
    yield
'''
@pytest.fixture(scope="session")
#@allure.title("set_window_size")
def browser_open_setting():
    browser = setup_browser
    #registration_form.given_opened(browser)
    browser.driver.set_window_size(1920, 1500) #размер окна важен    

def test_github(browser_open_setting):
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
