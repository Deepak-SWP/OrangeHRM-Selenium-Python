from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import URL


class LoginPage:

    username = (
        By.NAME,
        "username"
    )

    password = (
        By.NAME,
        "password"
    )

    login_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    invalid_message = (
        By.XPATH,
        "//p[text()='Invalid credentials']"
    )

    forgot_password_link = (
        By.XPATH,
        "//p[text()='Forgot your password? ']"
    )

    forgot_username = (
        By.NAME,
        "username"
    )

    reset_password_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def __init__(self, driver):

        self.driver = driver

    def open(self):

        self.driver.get(URL)

    def login(self, uname, pwd):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(
                self.username
            )
        ).send_keys(uname)

        self.driver.find_element(
            *self.password
        ).send_keys(pwd)

        self.driver.find_element(
            *self.login_btn
        ).click()

    def verify_invalid_login(self):

        wait = WebDriverWait(self.driver, 20)

        return wait.until(
            EC.visibility_of_element_located(
                self.invalid_message
            )
        ).is_displayed()

    def click_forgot_password(self):

        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.element_to_be_clickable(
                self.forgot_password_link
            )
        ).click()

    def enter_forgot_username(self):

        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.visibility_of_element_located(
                self.forgot_username
            )
        ).send_keys("Admin")

    def click_reset_password(self):

        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.element_to_be_clickable(
                self.reset_password_button
            )
        ).click()

    def verify_reset_message(self):
        return "requestResetPassword" in self.driver.current_url