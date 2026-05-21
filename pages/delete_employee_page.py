from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class DeleteEmployeePage:
    """Delete Employee Functionality"""

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def open_pim(self):
        """Open PIM Module"""

        try:

            logger.info("Opening PIM Module")

            pim = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='PIM']")
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                pim
            )

            logger.info("PIM Module Opened Successfully")

        except Exception as e:

            logger.error(f"PIM Module Opening Failed: {e}")

            raise

    def open_employee_list(self):
        """Open Employee List"""

        try:

            logger.info("Opening Employee List")

            employee_list = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[text()='Employee List']")
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                employee_list
            )

            logger.info("Employee List Opened Successfully")

        except Exception as e:

            logger.error(f"Employee List Opening Failed: {e}")

            raise

    def select_employee_record(self):
        """Select Employee Record"""

        try:

            logger.info("Selecting Employee Record")

            employee_box = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "(//input[@placeholder='Type for hints...'])[1]"
                    )
                )
            )

            employee_box.clear()

            employee_box.send_keys("Deepak")

            logger.info("Employee Record Selected Successfully")

        except Exception as e:

            logger.error(f"Employee Record Selection Failed: {e}")

            raise

    def click_delete_button(self):
        """Click Delete Button"""

        try:

            logger.info("Clicking Search Button")

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

            logger.info("Waiting For Loader To Disappear")

            self.wait.until(
                EC.invisibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        "oxd-loading-spinner"
                    )
                )
            )

            self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[@class='oxd-table-body']"
                    )
                )
            )

            logger.info("Employee Table Loaded Successfully")

            delete_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "(//i[contains(@class,'bi-trash')])[1]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                delete_btn
            )

            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "(//i[contains(@class,'bi-trash')])[1]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                delete_btn
            )

            logger.info("Delete Button Clicked Successfully")

        except Exception as e:

            logger.error(f"Delete Button Click Failed: {e}")

            raise

    def confirm_delete_action(self):
        """Confirm Delete Action"""

        try:

            logger.info("Confirming Delete Action")

            yes_delete = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[normalize-space()='Yes, Delete']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                yes_delete
            )

            logger.info("Employee Deleted Successfully")

        except Exception as e:

            logger.error(f"Delete Confirmation Failed: {e}")

            raise

    def verify_delete_success(self):
        """Verify Employee Delete Success"""

        try:

            logger.info("Verifying Employee Delete Success")

            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//h6[text()='PIM']"
                    )
                )
            )

            result = (
                "viewEmployeeList"
                in self.driver.current_url
            )

            logger.info("Employee Delete Verification Successful")

            return result

        except Exception as e:

            logger.error(f"Employee Delete Verification Failed: {e}")

            return False