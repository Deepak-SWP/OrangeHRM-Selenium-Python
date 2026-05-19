import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_text = (
        By.XPATH,
        "//h6[text()='Dashboard']"
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

        self.wait = WebDriverWait(driver, 30)

    # verify dashboard page
    def verify_dashboard(self):

        time.sleep(5)

        dashboard_elements = self.driver.find_elements(
            By.XPATH,
            "//h6[text()='Dashboard']"
        )

        return len(dashboard_elements) > 0

    # click profile dropdown
    def click_profile(self):

        profile = self.wait.until(
            EC.element_to_be_clickable(
                self.profile_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            profile
        )

        time.sleep(2)

    # click logout
    def click_logout(self):

        logout = self.wait.until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout
        )

        time.sleep(5)

    # verify login page after logout
    def verify_login_page(self):

        login_elements = self.driver.find_elements(
            By.XPATH,
            "//h5[text()='Login']"
        )

        return len(login_elements) > 0