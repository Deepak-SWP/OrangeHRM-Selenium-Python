import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class LeaveSearchPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def click_leave(self):

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

        time.sleep(5)

    def search_leave_records(self):

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

        time.sleep(5)

    def verify_leave_records(self):

        records = self.driver.find_elements(
            By.XPATH,
            "//div[@class='oxd-table-card']"
        )

        return len(records) > 0