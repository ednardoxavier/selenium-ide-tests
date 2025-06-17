from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test04iTrackCadastro:
def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.vars = {}

def teardown_method(self, method):
        self.driver.quit()


def test_04iTrackCadastro(self):
        self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
        self.driver.set_window_size(1722, 1034)
        self.driver.find_element(By.CSS_SELECTOR, ".mui-69i1ev").click()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-settings-link .MuiTypography-root").click()
        element = self.driver.find_element(By.ID, "create-dealer-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "mui-p-76691-T-users").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "create-user-button").click()
        self.driver.find_element(By.ID, ":r4i:").send_keys("Lucas Sicuto Teste")
        self.driver.find_element(By.ID, ":r4j:").send_keys("087.532")
        self.driver.find_element(By.ID, ":r4j:").send_keys("385.191.783-91")
        self.driver.find_element(By.ID, ":r4k:").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSizeMedium")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, ":r4k:").send_keys("lucassicuto12@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSizeMedium").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, ":r4d:")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".\\__variable_51684b").click()
        self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(2)").click()
        element = self.driver.find_element(By.ID, ":r4d:")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".\\__variable_51684b").click()
        self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1)").click()
        self.driver.find_element(By.ID, "dealer-autocomplete-input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#dealer-autocomplete-input-option-1 .MuiTypography-body2").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSizeMedium")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()
      
