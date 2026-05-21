from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class SearchEmployeePage:
    """Search Employee Functionality"""

    pim_menu = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    employee_name = (
        By.XPATH,
        "(//input[@placeholder='Type for hints...'])[1]"
    )

    search_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    employee_record = (
        By.XPATH,
        "//div[@class='oxd-table-body']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_pim(self):
        """Click PIM Module"""

        try:

            logger.info("Clicking PIM Module")

            pim = self.wait.until(
                EC.element_to_be_clickable(
                    self.pim_menu
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

    def search_employee(self):
        """Search Employee Record"""

        try:

            logger.info("Searching Employee")

            employee_input = self.wait.until(
                EC.visibility_of_element_located(
                    self.employee_name
                )
            )

            employee_input.clear()

            employee_input.send_keys("Deepak")

            logger.info("Employee Name Entered Successfully")

        except Exception as e:

            logger.error(f"Employee Search Failed: {e}")

            raise

    def click_search(self):
        """Click Search Button"""

        try:

            logger.info("Clicking Search Button")

            search_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.search_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                search_btn
            )

            logger.info("Search Button Clicked Successfully")

        except Exception as e:

            logger.error(f"Search Button Click Failed: {e}")

            raise

    def verify_employee(self):
        """Verify Employee Record"""

        try:

            logger.info("Verifying Employee Record")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.employee_record
                )
            )

            result = (
                "viewEmployeeList"
                in self.driver.current_url
            )

            logger.info("Employee Record Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Employee Verification Failed: {e}")

            return False