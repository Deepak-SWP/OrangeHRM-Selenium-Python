from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class LeavePage:

    leave_menu = (
        By.XPATH,
        "//span[text()='Leave']"
    )

    leave_text = (
        By.XPATH,
        "//h6[text()='Leave']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_leave_menu(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.leave_menu
            )
        ).click()

    def verify_leave_page(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.leave_text
            )
        ).is_displayed()