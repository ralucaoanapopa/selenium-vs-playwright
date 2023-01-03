import os

class BasePage:

    base_URL = "https://demoqa.com/"
    title = "ToolsQA"
    login_URL = base_URL + "login"
    profile_URL = base_URL + "profile"

    # credentials
    user_name = os.environ.get('USERNAME_QA')
    user_pass = os.environ.get('PASSWORD_QA')