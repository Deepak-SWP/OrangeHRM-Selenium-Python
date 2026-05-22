from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger

import random

import time


class EmployeePage:
    """Employee Management Functionality"""

    pim_menu = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    add_employee_btn = (
        By.XPATH,
        "//a[normalize-space()='Add Employee']"
    )

    first_name = (
        By.NAME,
        "firstName"
    )

    last_name = (
        By.NAME,
        "lastName"
    )

    employee_id = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    save_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_pim(self):
        """Click PIM menu"""

        try:

            logger.info("Clicking PIM Menu")

            self.wait.until(
                EC.element_to_be_clickable(
                    self.pim_menu
                )
            ).click()

            logger.info(
                "PIM Menu Clicked Successfully"
            )

        except Exception as e:

            logger.error(
                f"PIM Menu Click Failed: {e}"
            )

            raise

    def click_add_employee(self):
        """Click Add Employee button"""

        try:

            logger.info(
                "Clicking Add Employee Button"
            )

            add_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.add_employee_btn
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                add_btn
            )

            self.driver.execute_script(
                "arguments[0].click();",
                add_btn
            )

            logger.info(
                "Add Employee Button Clicked Successfully"
            )

        except Exception as e:

            logger.error(
                f"Add Employee Button Click Failed: {e}"
            )

            raise

    def enter_employee_details(self):
        """Enter Employee Details"""

        try:

            logger.info(
                "Entering Employee Details"
            )

            random_number = random.randint(
                1000,
                9999
            )

            timestamp_employee_id = str(
                int(time.time())
            )[-6:]

            first_name_input = self.wait.until(
                EC.element_to_be_clickable(
                    self.first_name
                )
            )

            first_name_input.clear()

            first_name_input.send_keys(
                f"Deepak{random_number}"
            )

            last_name_input = self.wait.until(
                EC.element_to_be_clickable(
                    self.last_name
                )
            )

            last_name_input.clear()

            last_name_input.send_keys(
                "Dusa"
            )

            employee_id_input = self.wait.until(
                EC.element_to_be_clickable(
                    self.employee_id
                )
            )

            employee_id_input.clear()

            employee_id_input.send_keys(
                timestamp_employee_id
            )

            logger.info(
                "Employee Details Entered Successfully"
            )

        except Exception as e:

            logger.error(
                f"Entering Employee Details Failed: {e}"
            )

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

            logger.info(
                "Save Button Clicked Successfully"
            )

        except Exception as e:

            logger.error(
                f"Save Button Click Failed: {e}"
            )

            raise

    def verify_employee_added(self):
        """Verify Employee Added Successfully"""

        try:

            logger.info(
                "Verifying Employee Added"
            )

            self.wait.until(
                EC.any_of(
                    EC.url_contains(
                        "viewPersonalDetails"
                    ),
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//h6[text()='Personal Details']"
                        )
                    )
                )
            )

            logger.info(
                "Employee Added Successfully"
            )

            return True

        except Exception as e:

            logger.error(
                f"Employee Verification Failed: {e}"
            )

            return False