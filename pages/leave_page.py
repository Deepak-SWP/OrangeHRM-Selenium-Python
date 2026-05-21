from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class LeavePage:
    """Leave Module Functionality"""

    leave_menu = (
        By.XPATH,
        "//span[text()='Leave']"
    )

    leave_text = (
        By.XPATH,
        "//h6[text()='Leave']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_leave_menu(self):
        """Click Leave Menu"""

        try:

            logger.info("Clicking Leave Menu")

            leave = self.wait.until(
                EC.element_to_be_clickable(
                    self.leave_menu
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                leave
            )

            logger.info("Leave Menu Clicked Successfully")

        except Exception as e:

            logger.error(f"Leave Menu Click Failed: {e}")

            raise

    def verify_leave_page(self):
        """Verify Leave Page"""

        try:

            logger.info("Verifying Leave Page")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.leave_text
                )
            )

            result = (
                "leave"
                in self.driver.current_url.lower()
            )

            logger.info("Leave Page Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Leave Page Verification Failed: {e}")

            return False