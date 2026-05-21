from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class LeaveSearchPage:
    """Leave Search Functionality"""

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def click_leave(self):
        """Click Leave Menu"""

        try:

            logger.info("Clicking Leave Menu")

            leave = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[text()='Leave']"
                    )
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

    def search_leave_records(self):
        """Search Leave Records"""

        try:

            logger.info("Searching Leave Records")

            self.wait.until(
                EC.invisibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        "oxd-form-loader"
                    )
                )
            )

            search_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@type='submit']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                search_btn
            )

            logger.info("Leave Records Search Successful")

        except Exception as e:

            logger.error(f"Leave Search Failed: {e}")

            raise

    def verify_leave_records(self):
        """Verify Leave Records"""

        try:

            logger.info("Verifying Leave Records")

            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//h6[text()='Leave']"
                    )
                )
            )

            result = (
                "viewLeaveList"
                in self.driver.current_url
            )

            logger.info("Leave Records Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Leave Records Verification Failed: {e}")

            return False