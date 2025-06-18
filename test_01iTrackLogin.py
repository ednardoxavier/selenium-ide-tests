import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir=/tmp/chrome-profile-{id(self)}")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def wait_and_click(self, by, selector):
        element = self.wait.until(EC.element_to_be_clickable((by, selector)))
        element.click()
        return element

    def wait_and_send_keys(self, by, selector, text):
        element = self.wait.until(EC.visibility_of_element_located((by, selector)))
        element.send_keys(text)
        return element

    def move_to_element(self, by, selector):
        element = self.wait.until(EC.presence_of_element_located((by, selector)))
        self.actions.move_to_element(element).perform()
        return element

class Test01iTrackLogin(BaseTest):

    def test_01iTrackLogin(self):
        self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
        self.driver.set_window_size(1722, 1034)

        self.wait_and_click(By.CSS_SELECTOR, "#products-agco-reman img")
        self.move_to_element(By.ID, "auth-user-tower")
        self.wait_and_click(By.ID, "auth-user-tower")
        self.wait_and_send_keys(By.ID, "signin-email-input", "agco@esparta.io")
        self.wait_and_send_keys(By.ID, "signin-password-input", "admin")
        self.wait_and_click(By.ID, "signin-remember-checkbox")
        self.move_to_element(By.ID, "signin-submit-button")
        self.wait_and_click(By.ID, "signin-submit-button")
        self.move_to_element(By.CSS_SELECTOR, "body")
        self.wait_and_click(By.ID, "drawer-dashboard-link")
