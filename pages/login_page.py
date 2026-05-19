import time

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

        self.wait = WebDriverWait(driver, 30)

    def open(self):

        self.driver.get(URL)

    def login(self, uname, pwd):

        username = self.wait.until(
            EC.visibility_of_element_located(
                self.username
            )
        )

        password = self.wait.until(
            EC.visibility_of_element_located(
                self.password
            )
        )

        username.clear()
        username.send_keys(uname)

        password.clear()
        password.send_keys(pwd)

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.login_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

        time.sleep(8)

    def verify_invalid_login(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.invalid_message
            )
        ).is_displayed()

    def click_forgot_password(self):

        forgot = self.wait.until(
            EC.element_to_be_clickable(
                self.forgot_password_link
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            forgot
        )

        time.sleep(3)

    def enter_forgot_username(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.forgot_username
            )
        ).send_keys("Admin")

    def click_reset_password(self):

        reset_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.reset_password_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            reset_btn
        )

        time.sleep(5)

    def verify_reset_message(self):

        return "requestResetPassword" in self.driver.current_url