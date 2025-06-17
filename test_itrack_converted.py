from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class 01-itrack_loginTest:
    def setup_method(self, method):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('https://reman.esparta.io')

    def teardown_method(self, method):
        self.driver.quit()

    def test_main(self):
        # Comando não tratado: setWindowSize 1722x1034
        self.driver.find_element(By.CSS, "#products-agco-reman img").click()
        # Comando não tratado: mouseOver id=auth-user-tower
        self.driver.find_element(By.ID, "auth-user-tower").click()
        self.driver.find_element(By.ID, "signin-email-input").send_keys("agco@esparta.io")
        self.driver.find_element(By.ID, "signin-password-input").send_keys("admin")
        self.driver.find_element(By.ID, "signin-remember-checkbox").click()
        # Comando não tratado: mouseOver id=signin-submit-button
        self.driver.find_element(By.ID, "signin-submit-button").click()
        # Comando não tratado: mouseOut id=signin-submit-button
        self.driver.find_element(By.ID, "drawer-dashboard-link").click()