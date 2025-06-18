from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test02iTrackLoginPerformance:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()


      def test_02iTrackLoginPerformance(self):
        self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
        self.driver.set_window_size(1722, 1034)
        element = self.driver.find_element(By.ID, "drawer-settings-link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".mui-9wjka2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-settings-link .MuiTypography-root").click()
        self.driver.find_element(By.ID, "mui-p-86671-T-transporters").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "mui-p-86671-T-users").click()
        self.driver.find_element(By.ID, "mui-p-86671-T-receivers").click()
        self.driver.find_element(By.ID, "mui-p-86671-T-docs").click()
        self.driver.find_element(By.ID, "mui-p-86671-T-remans").click()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()
      
