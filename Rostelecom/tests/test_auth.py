# tests/test_auth.py
import pytest
from pages.auth_page import AuthPage
from data.test_data import valid_phone, valid_email, valid_login, valid_password, valid_account, invalid_password
from settings import ELK_WEB, KEY_WEB, START_WEB

@pytest.mark.auth
def test_auth_by_phone_success(driver):
    page = AuthPage(driver)
    page.open()
    page.select_tab("phone")
    page.enter_username(valid_phone)
    page.enter_password(valid_password)
    page.click_login()
    page.wait_for_redirect(ELK_WEB)  # редирект на ЕЛК Web

@pytest.mark.auth
def test_auth_by_email_success(driver):
    page = AuthPage(driver)
    page.open()
    page.select_tab("email")
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.click_login()
    page.wait_for_redirect(KEY_WEB)  # редирект на Ключ Web

@pytest.mark.auth
def test_auth_by_login_success(driver):
    page = AuthPage(driver)
    page.open()
    page.select_tab("login")
    page.enter_username(valid_login)
    page.enter_password(valid_password)
    page.click_login()
    page.wait_for_redirect(START_WEB)  # редирект на Старт Web


@pytest.mark.auth
def test_auth_by_account_success(driver): #TC04 — авторизация по лицевому счету (ЕЛК Web)
    page = AuthPage(driver)
    page.open()
    page.select_tab("account")
    page.enter_username(valid_account)
    page.enter_password(valid_password)
    page.click_login()
    page.wait_for_redirect(ELK_WEB)  # редирект на ЕЛК


@pytest.mark.auth
def test_auth_wrong_password(driver): #TC07 — авторизация с неверным паролем
    page = AuthPage(driver)
    page.open()
    page.select_tab("phone")
    page.enter_username(valid_phone)
    page.enter_password(invalid_password)
    page.click_login()
    assert "Неверный логин или пароль" in page.get_error_text()

@pytest.mark.auth
def test_auth_empty_fields(driver): #TC08 — авторизация с пустыми полями
    page = AuthPage(driver)
    page.open()
    page.select_tab("email")
    page.click_login()
    error = page.get_error_text()
    assert error != "", "Ошибка: сообщение об ошибке отсутствует при пустых полях" # может быть "Введите логин", "Поле обязательно" и т.п.
