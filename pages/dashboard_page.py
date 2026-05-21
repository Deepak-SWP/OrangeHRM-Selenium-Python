from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class DashboardPage:
    """Dashboard and Logout Functionality"""

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

    def verify_dashboard(self):
        """Verify Dashboard Page"""

        try:

            logger.info("Verifying Dashboard Page")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.dashboard_text
                )
            )

            result = (
                "dashboard"
                in self.driver.current_url.lower()
            )

            logger.info("Dashboard Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Dashboard Verification Failed: {e}")

            return False

    def click_profile(self):
        """Click Profile Dropdown"""

        try:

            logger.info("Clicking Profile Menu")

            profile = self.wait.until(
                EC.element_to_be_clickable(
                    self.profile_menu
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                profile
            )

            logger.info("Profile Menu Clicked Successfully")

        except Exception as e:

            logger.error(f"Profile Menu Click Failed: {e}")

            raise

    def click_logout(self):
        """Click Logout Button"""

        try:

            logger.info("Clicking Logout Button")

            logout = self.wait.until(
                EC.element_to_be_clickable(
                    self.logout_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                logout
            )

            logger.info("Logout Successful")

        except Exception as e:

            logger.error(f"Logout Failed: {e}")

            raise

    def verify_login_page(self):
        """Verify Login Page After Logout"""

        try:

            logger.info("Verifying Login Page")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.login_page_text
                )
            )

            result = (
                "login"
                in self.driver.current_url.lower()
            )

            logger.info("Login Page Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Login Page Verification Failed: {e}")

            return False