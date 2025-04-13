# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, value):
        el = self.find(locator)
        el.clear()
        el.send_keys(value)

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def get_text(self, locator):
        return self.find(locator).text

    def wait_for_url(self, expected_part):
        self.wait.until(lambda driver: expected_part in driver.current_url)
