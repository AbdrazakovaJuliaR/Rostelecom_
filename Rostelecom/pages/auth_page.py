# pages/auth_page.py
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators

class AuthPage(BasePage):
    def open(self, url="https://b2c.passport.rt.ru/"):
        super().open(url)

    def select_tab(self, tab_name):
        tabs = {
            "phone": AuthLocators.TAB_PHONE,
            "email": AuthLocators.TAB_EMAIL,
            "login": AuthLocators.TAB_LOGIN,
            "account": AuthLocators.TAB_ACCOUNT,
        }
        self.click(tabs[tab_name])

    def enter_username(self, value):
        self.type(AuthLocators.INPUT_USERNAME, value)

    def enter_password(self, value):
        self.type(AuthLocators.INPUT_PASSWORD, value)

    def click_login(self):
        self.click(AuthLocators.BTN_LOGIN)

    def wait_for_redirect(self, expected_url_part):
        self.wait.until(lambda driver: expected_url_part in driver.current_url)

    def get_error_text(self):
        from selenium.webdriver.common.by import By
        return self.get_text((By.ID, "form-error-message"))
