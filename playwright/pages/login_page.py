from playwright.sync_api import Page

from pages.base import BasePage

class LoginPage(BasePage):

    username_input_id = "input[id='userName']"
    password_input_id = "input[id='password']"
    login_btn_id = "button[id='login']"

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def load(self):
        self.page.goto(self.login_URL)

    def login_form(self, username, password):
        self.get_username().fill(username)
        self.get_password().fill(password)
        self.get_login_btn().click()

    def get_username(self):
        return self.page.locator(self.username_input_id)

    def get_password(self):
        return self.page.locator(self.password_input_id)

    def get_login_btn(self):
        return self.page.locator(self.login_btn_id)