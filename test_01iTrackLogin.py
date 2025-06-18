import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test01iTrackLogin:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir=/tmp/chrome-profile-{id(self)}")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self, method):
        self.driver.quit()

    def test_01iTrackLogin(self):
        try:
            self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
            self.driver.set_window_size(1722, 1034)

            # Aguarda o clique no card "AGCO Reman"
            self.wait.until(EC.element_to_be_clickable((By.ID, "products-agco-reman"))).click()

            # Login
            self.wait.until(EC.presence_of_element_located((By.ID, "auth-user-tower"))).click()
            self.driver.find_element(By.ID, "signin-email-input").send_keys("agco@esparta.io")
            self.driver.find_element(By.ID, "signin-password-input").send_keys("admin")
            self.driver.find_element(By.ID, "signin-remember-checkbox").click()

            # Submeter login
            self.driver.find_element(By.ID, "signin-submit-button").click()

            # Aguarda o menu principal e clica no dashboard
            self.wait.until(EC.element_to_be_clickable((By.ID, "drawer-dashboard-link"))).click()

        except Exception as e:
            self.driver.save_screenshot("screenshot_error.png")
            raise e
