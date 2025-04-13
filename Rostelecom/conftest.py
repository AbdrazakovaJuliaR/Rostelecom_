
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # для CI/CD; можно убрать при локальной отладке
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

#добавим вторую фикстуру
@pytest.fixture
def driver_no_cookies():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.cookies": 2  # disable cookies
    })
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
