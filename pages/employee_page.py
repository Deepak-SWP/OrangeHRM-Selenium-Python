from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:

    pim_menu = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    add_employee_btn = (
        By.XPATH,
        "//a[text()='Add Employee']"
    )

    first_name = (
        By.NAME,
        "firstName"
    )

    last_name = (
        By.NAME,
        "lastName"
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

        self.wait.until(
            EC.element_to_be_clickable(
                self.pim_menu
            )
        ).click()

    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.add_employee_btn
            )
        ).click()

    def enter_employee_details(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        ).send_keys("Deepak")

        self.driver.find_element(
            *self.last_name
        ).send_keys("Kumar")

    def click_save(self):

    # Wait for loader to disappear
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "oxd-form-loader")
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

    def verify_employee_added(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        ).is_displayed()