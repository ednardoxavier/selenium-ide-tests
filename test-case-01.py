# test-case-01.py
# Adaptado para rodar com webdriver-manager e em modo headless

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestTestCase01:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test_case_01(self):
        self.driver.get("https://demoblaze.com/")
        self.driver.find_element(By.ID, "itemc").click()
        self.driver.find_element(By.ID, "nava").click()
        print("Teste executado com sucesso.")
