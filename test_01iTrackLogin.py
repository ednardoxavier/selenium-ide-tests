import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test01iTrackLogin():
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Evita conflito com perfis de usuário
        options.add_argument(f"--user-data-dir=/tmp/chrome-profile-{id(self)}")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_01iTrackLogin(self):
        self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
        self.driver.set_window_size(1722, 1034)
        self.driver.find_element(By.CSS_SELECTOR, "#products-agco-reman img").click()
        element = self.driver.find_element(By.ID, "auth-user-tower")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "auth-user-tower").click()
        self.driver.find_element(By.ID, "signin-email-input").send_keys("agco@esparta.io")
        self.driver.find_element(By.ID, "signin-password-input").send_keys("admin")
        self.driver.find_element(By.ID, "teste").click()
        element = self.driver.find_element(By.ID, "signin-submit-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "signin-submit-button").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "drawer-dashboard-link").click()
