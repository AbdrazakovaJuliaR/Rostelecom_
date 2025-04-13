# pages/register_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    def open(self, url="https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"):
        super().open(url)

    def enter_first_name(self, value):
        self.type((By.NAME, "firstName"), value)

    def enter_last_name(self, value):
        self.type((By.NAME, "lastName"), value)

    def select_region(self, value="Москва г"):
        region_input = (By.CSS_SELECTOR, ".rt-select .rt-input__input")
        self.click(region_input)
        self.type(region_input, value)
        self.click((By.XPATH, f"//span[text()='{value}']"))

    def enter_email_or_phone(self, value):
        self.type((By.ID, "address"), value)

    def enter_password(self, value):
        self.type((By.ID, "password"), value)
        self.type((By.ID, "password-confirm"), value)

    def click_continue(self):
        self.click((By.NAME, "register"))

    def wait_for_code_input(self):
        self.find((By.CSS_SELECTOR, ".otp-input-container"))
