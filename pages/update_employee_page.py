from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class UpdateEmployeePage:
    """Update Employee Functionality"""

    pim_menu = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    employee_record = (
        By.XPATH,
        "(//div[@class='oxd-table-card'])[1]"
    )

    nickname_field = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    save_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    success_message = (
        By.XPATH,
        "//h6[text()='Personal Details']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_pim(self):
        """Click PIM Menu"""

        try:

            logger.info("Clicking PIM Menu")

            pim = self.wait.until(
                EC.element_to_be_clickable(
                    self.pim_menu
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                pim
            )

            logger.info("PIM Menu Clicked Successfully")

        except Exception as e:

            logger.error(f"PIM Menu Click Failed: {e}")

            raise

    def open_employee_record(self):
        """Open Employee Record"""

        try:

            logger.info("Opening Employee Record")

            record = self.wait.until(
                EC.element_to_be_clickable(
                    self.employee_record
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                record
            )

            logger.info("Employee Record Opened Successfully")

        except Exception as e:

            logger.error(f"Employee Record Opening Failed: {e}")

            raise

    def update_employee_details(self):
        """Update Employee Details"""

        try:

            logger.info("Updating Employee Details")

            field = self.wait.until(
                EC.visibility_of_element_located(
                    self.nickname_field
                )
            )

            field.clear()

            field.send_keys("Deepak")

            logger.info("Employee Details Updated Successfully")

        except Exception as e:

            logger.error(f"Employee Update Failed: {e}")

            raise

    def click_save(self):
        """Click Save Button"""

        try:

            logger.info("Clicking Save Button")

            self.wait.until(
                EC.invisibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        "oxd-form-loader"
                    )
                )
            )

            save_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.save_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                save_btn
            )

            logger.info("Save Button Clicked Successfully")

        except Exception as e:

            logger.error(f"Save Button Click Failed: {e}")

            raise

    def verify_update(self):
        """Verify Employee Update"""

        try:

            logger.info("Verifying Employee Update")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.success_message
                )
            )

            result = (
                "viewPersonalDetails"
                in self.driver.current_url
            )

            logger.info("Employee Updated Successfully")

            return result

        except Exception as e:

            logger.error(f"Employee Update Verification Failed: {e}")

            return False