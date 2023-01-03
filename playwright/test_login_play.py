from playwright.sync_api import expect
from pages.base import BasePage
from pages.login_page import LoginPage
import pytest

base = BasePage()

@pytest.fixture(scope="session", autouse=True)
def before_all_after_all(playwright):
    # create context for all tests
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()
    page.goto(base.base_URL)

    yield page
    page.close()


def test_login_with_valid_credentials(before_all_after_all):
    page = before_all_after_all
    expect(page).to_have_title(base.title)

    login_page = LoginPage(page)
    login_page.load()

    expect(page).to_have_url(base.login_URL)
    expect(login_page.get_username()).to_be_visible() is True
    expect(login_page.get_password()).to_be_visible() is True
    expect(login_page.get_login_btn()).to_be_visible() is True

    login_page.login_form(base.user_name, base.user_pass)
    expect(page).to_have_url(base.profile_URL)