#TC12 — регистрация по почте

import pytest
from pages.register_page import RegisterPage
from data.test_data import new_email, new_first_name, new_last_name, new_password, new_phone
from conftest import driver

@pytest.mark.register
def test_register_with_email(driver):
    page = RegisterPage(driver)
    page.open()
    page.enter_first_name(new_first_name)
    page.enter_last_name(new_last_name)
    page.select_region("Москва г")
    page.enter_email_or_phone(new_email)
    page.enter_password(new_password)
    page.click_continue()
    page.wait_for_code_input()

#TC13 — регистрация по телефону

@pytest.mark.register
def test_register_with_phone(driver):
    page = RegisterPage(driver)
    page.open()
    page.enter_first_name(new_first_name)
    page.enter_last_name(new_last_name)
    page.select_region("Москва г")
    page.enter_email_or_phone(new_phone)
    page.enter_password(new_password)
    page.click_continue()
    page.wait_for_code_input()
