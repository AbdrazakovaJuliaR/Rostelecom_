# pages/recovery_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RecoveryPage(BasePage):
    def open(self, url="https://b2c.passport.rt.ru/"):
        super().open(url)
        self.click((By.ID, "forgot_password"))

    def select_tab(self, tab_name):
        tabs = {
            "phone": (By.ID, "t-btn-tab-phone"),
            "email": (By.ID, "t-btn-tab-mail"),
        }
        self.click(tabs[tab_name])

    def enter_contact(self, value):
        self.type((By.ID, "username"), value)

    def enter_captcha(self, text="1234"):
        self.type((By.ID, "captcha"), text)

    def click_next(self):
        self.click((By.ID, "reset"))

    def wait_for_code_page(self):
        self.find((By.ID, "rt-code-0"))
