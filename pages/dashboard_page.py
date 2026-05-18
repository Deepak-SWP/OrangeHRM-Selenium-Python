from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_text = (By.XPATH, "//h6")

    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard(self):

        wait = WebDriverWait(self.driver, 20)

        element = wait.until(
            EC.visibility_of_element_located(self.dashboard_text)
        )

        return element.is_displayed()