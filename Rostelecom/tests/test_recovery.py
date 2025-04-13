# TC09 — восстановление по телефону
import pytest
from pages.recovery_page import RecoveryPage
from data.test_data import recovery_phone, recovery_email
from conftest import driver

@pytest.mark.recovery
def test_password_recovery_phone(driver):
    page = RecoveryPage(driver)
    page.open()
    page.select_tab("phone")
    page.enter_contact(recovery_phone)
    page.enter_captcha("1234")
    page.click_next()
    page.wait_for_code_page()

#TC10 — восстановление по почте

@pytest.mark.recovery
def test_password_recovery_email(driver):
    page = RecoveryPage(driver)
    page.open()
    page.select_tab("email")
    page.enter_contact(recovery_email)
    page.enter_captcha("1234")
    page.click_next()
    page.wait_for_code_page()
