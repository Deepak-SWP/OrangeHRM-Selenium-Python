import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class EmployeeListPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def click_pim(self):

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

        time.sleep(3)

    def open_employee_list(self):

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

        time.sleep(5)

    def verify_employee_records(self):

        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='oxd-table-card']"
                )
            )
        )

        records = self.driver.find_elements(
            By.XPATH,
            "//div[@class='oxd-table-card']"
        )

        return len(records) > 0