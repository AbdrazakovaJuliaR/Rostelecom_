# locators/auth_locators.py
from selenium.webdriver.common.by import By

class AuthLocators:
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_ACCOUNT = (By.ID, "t-btn-tab-ls")
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "kc-login")
