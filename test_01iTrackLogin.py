
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test01iTrackLogin:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.set_window_size(1722, 1034)
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self, method):
        self.driver.quit()

    def test_01iTrackLogin(self):
        try:
            self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
            self.wait.until(EC.element_to_be_clickable((By.ID, "products-agco-reman"))).click()
            element = self.wait.until(EC.presence_of_element_located((By.ID, "auth-user-tower")))
            ActionChains(self.driver).move_to_element(element).perform()
            self.driver.find_element(By.ID, "auth-user-tower").click()
            self.driver.find_element(By.ID, "signin-email-input").send_keys("agco@esparta.io")
            self.driver.find_element(By.ID, "signin-password-input").send_keys("admin")
            self.driver.find_element(By.ID, "signin-remember-checkbox").click()
            self.driver.find_element(By.ID, "signin-submit-button").click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "drawer-dashboard-link"))).click()
        except Exception as e:
            self.driver.save_screenshot("screenshot_error.png")
            raise e
