from selenium.webdriver.common.by import By
from pages.base import BasePage

base = BasePage()

class LoginPage:

    username_input_id = "userName"
    password_input_id = "password"
    login_btn_id = "login"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(base.login_URL)

    def login_form(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login_btn().click()

    def get_username(self):
        return self.browser.find_element(By.ID, self.username_input_id)

    def get_password(self):
        return self.browser.find_element(By.ID, self.password_input_id)

    def get_login_btn(self):
        return self.browser.find_element(By.ID, self.login_btn_id)
