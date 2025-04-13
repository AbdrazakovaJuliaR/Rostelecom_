
import pytest
from pages.temp_code_page import TempCodePage
from data.test_data import otp_phone, otp_email
from conftest import driver

#TC05 — вход по временному коду (телефон)
@pytest.mark.otp
def test_otp_login_by_phone(driver):
    page = TempCodePage(driver)
    page.open()
    page.enter_contact(otp_phone)
    page.click_get_code()
    page.wait_for_code_input()

#TC06 — вход по временному коду (почта)

@pytest.mark.otp
def test_otp_login_by_email(driver):
    page = TempCodePage(driver)
    page.open()
    page.enter_contact(otp_email)
    page.click_get_code()
    page.wait_for_code_input()

