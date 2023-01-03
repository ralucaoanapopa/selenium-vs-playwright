import pytest
from selenium.webdriver import Chrome
from pages.base import BasePage
from pages.login import LoginPage

base = BasePage()

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup(browser):
    browser.get(base.base_URL)


def test_login_valid_credentials(browser, setup):
    assert browser.title == base.title
    login = LoginPage(browser)
    login.load()
    assert browser.current_url == base.login_URL
    assert login.get_username().is_displayed() is True
    assert login.get_password().is_displayed() is True
    assert login.get_login_btn().is_displayed() is True