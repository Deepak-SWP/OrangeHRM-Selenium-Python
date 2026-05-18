from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class SearchEmployeePage:

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

        self.wait.until(
            EC.element_to_be_clickable(
                self.pim_menu
            )
        ).click()

    def search_employee(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.employee_name
            )
        ).send_keys("Deepak")

    def click_search(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.search_button
            )
        ).click()

    def verify_employee(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.employee_record
            )
        ).is_displayed()