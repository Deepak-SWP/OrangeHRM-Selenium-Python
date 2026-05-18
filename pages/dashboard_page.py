from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_text = (
        By.XPATH,
        "//h6"
    )

    profile_menu = (
        By.CLASS_NAME,
        "oxd-userdropdown-name"
    )

    logout_button = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    login_page_text = (
        By.XPATH,
        "//h5[text()='Login']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def verify_dashboard(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.dashboard_text
            )
        )

        return element.is_displayed()

    def click_profile(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.profile_menu
            )
        ).click()

    def click_logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        ).click()

    def verify_login_page(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.login_page_text
            )
        ).is_displayed()