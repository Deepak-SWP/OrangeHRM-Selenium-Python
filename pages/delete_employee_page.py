import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeleteEmployeePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # open PIM module
    def open_pim(self):

        pim = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            pim
        )

        time.sleep(3)

    # open employee list
    def open_employee_list(self):

        employee_list = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Employee List']")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            employee_list
        )

        time.sleep(3)

    # enter employee name
    def select_employee_record(self):

        employee_box = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='Type for hints...'])[1]"
                )
            )
        )

        employee_box.clear()

        employee_box.send_keys("manda")

        time.sleep(3)

    # click search and delete icon
    def click_delete_button(self):

        # search button
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

        time.sleep(6)

        # wait for employee table
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='oxd-table-body']"
                )
            )
        )

        time.sleep(3)

        # delete icon
        delete_btn = self.wait.until(
            EC.presence_of_element_located(
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

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_btn
        )

        time.sleep(5)

    # confirm delete popup
    def confirm_delete_action(self):

        yes_delete = self.wait.until(
            EC.presence_of_element_located(
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

        time.sleep(5)

    # verify success message
    def verify_delete_success(self):

        time.sleep(3)

        current_url = self.driver.current_url

        if "viewEmployeeList" in current_url:
            return True

        return False
    