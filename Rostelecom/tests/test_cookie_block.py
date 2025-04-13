# TC15 — тест cookie блокировки
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver_no_cookies

@pytest.mark.cookie
def test_cookie_block_popup(driver_no_cookies):
    driver_no_cookies.get("https://b2c.passport.rt.ru/")
    WebDriverWait(driver_no_cookies, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "card-container__title")))
    title = driver_no_cookies.find_element(By.CLASS_NAME, "card-container__title").text
    assert "Cookie отключены" in title, f"Ожидалось сообщение о cookie, получено: {title}"
