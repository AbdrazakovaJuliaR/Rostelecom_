# pages/temp_code_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TempCodePage(BasePage):
    def open(self, url="https://b2c.passport.rt.ru/"):
        super().open(url)
        self.click((By.ID, "back_to_otp_btn"))

    def enter_contact(self, value):
        self.type((By.ID, "address"), value)

    def click_get_code(self):
        self.click((By.ID, "otp_get_code"))

    def wait_for_code_input(self):
        self.find((By.ID, "rt-code-0"))
