from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestTestCase02:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test_case_02(self):
        self.driver.get("https://demoblaze.com/index.html#")
        self.driver.find_element(By.LINK_TEXT, "Monitors").click()
        self.driver.find_element(By.ID, "nava").click()
        print("Teste 02 executado com sucesso.")
