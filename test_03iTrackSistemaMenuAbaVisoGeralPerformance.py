from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test03iTrackSistemaMenuAbaVisoGeralPerformance:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_03iTrackSistemaMenuAbaVisoGeralPerformance(self):
        self.driver.get("https://reman.esparta.io/acesso?callbackUrl=https%3A%2F%2Freman.esparta.io%2F")
        self.driver.set_window_size(1722, 1034)

        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-settings-link .MuiTypography-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-settings-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-1cl7kxn .mui-e1wt8v").click()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".mui-16u4g7y .mui-e1wt8v")
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-17zvvlb").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "a > img")
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-16u4g7y .mui-e1wt8v").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-j093rn .mui-16f0ax0").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-f1xk5b .mui-e1wt8v").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-5j7ga1 .mui-16f0ax0").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-5qmmj5 .mui-e1wt8v").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-16978jq .mui-e1wt8v").click()

        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "drawer-dashboard-link").click()

        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-9wjka2 > .MuiBox-root").click()

        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-1w4gfva").click()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.ID, "drawer-dashboard-link")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-88w89i").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-1lk52ym .mui-e1wt8v").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mui-9pe607 .mui-16f0ax0").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#drawer-dashboard-link .MuiTypography-root").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element, 0, 0).perform()
