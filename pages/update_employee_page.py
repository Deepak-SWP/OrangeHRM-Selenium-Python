from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class UpdateEmployeePage:

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
        "//p[contains(text(),'Successfully Updated')]"
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

    def open_employee_record(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.employee_record
            )
        ).click()

    def update_employee_details(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.nickname_field
            )
        )

        field.clear()

        field.send_keys("Deepak")

    def click_save(self):

        self.wait.until(
        EC.invisibility_of_element_located(
            (
                By.CLASS_NAME,
                "oxd-form-loader"
            )
        )
    )

        self.wait.until(
        EC.element_to_be_clickable(
            self.save_button
        )
    ).click()

    def verify_update(self):

        success = self.wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'oxd-toast')]"
            )
        )
    )

        return success.is_displayed()