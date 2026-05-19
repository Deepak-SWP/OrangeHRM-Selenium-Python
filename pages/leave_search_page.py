import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class LeaveSearchPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    # click Leave menu
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

    # search leave records
    def search_leave_records(self):

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

        time.sleep(5)

    # verify records
    def verify_leave_records(self):

        time.sleep(3)

        current_url = self.driver.current_url

        if "viewLeaveList" in current_url:
            return True

        return False