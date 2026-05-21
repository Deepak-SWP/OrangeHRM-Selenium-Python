from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class EmployeeListPage:
    """Employee List Validation Functionality"""

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def click_pim(self):
        """Click PIM Module"""

        try:

            logger.info("Clicking PIM Module")

            pim = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[text()='PIM']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                pim
            )

            logger.info("PIM Module Clicked Successfully")

        except Exception as e:

            logger.error(f"PIM Module Click Failed: {e}")

            raise

    def open_employee_list(self):
        """Open Employee List Page"""

        try:

            logger.info("Opening Employee List Page")

            employee_list = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//a[text()='Employee List']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                employee_list
            )

            logger.info("Employee List Page Opened Successfully")

        except Exception as e:

            logger.error(f"Opening Employee List Failed: {e}")

            raise

    def verify_employee_records(self):
        """Verify Employee Records"""

        try:

            logger.info("Verifying Employee Records")

            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//h6[text()='PIM']"
                    )
                )
            )

            records = self.driver.find_elements(
                By.XPATH,
                "//div[@class='oxd-table-card']"
            )

            result = (
                len(records) > 0
                and
                "viewEmployeeList"
                in self.driver.current_url
            )

            logger.info("Employee Records Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Employee Records Verification Failed: {e}")

            return False