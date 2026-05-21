from utils.logger import logger

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.config import URL


class LoginPage:
    """Login and Forgot Password Functionality"""

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

    dashboard_text = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def open(self):
        """Open OrangeHRM Application"""

        try:

            logger.info("Opening OrangeHRM Application")

            self.driver.get(URL)

            logger.info(
                "OrangeHRM Application Opened Successfully"
            )

        except Exception as e:

            logger.error(
                f"Application Opening Failed: {e}"
            )

            raise

    def login(self, uname, pwd):
        """Perform Login Action"""

        try:

            logger.info("Performing Login")

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

            logger.info(
                "Login Button Clicked Successfully"
            )

        except Exception as e:

            logger.error(f"Login Failed: {e}")

            raise

    def verify_dashboard_login(self):
        """Verify Successful Login"""

        try:

            logger.info("Verifying Dashboard Login")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.dashboard_text
                )
            )

            result = (
                "dashboard"
                in self.driver.current_url.lower()
            )

            logger.info("Dashboard Login Verified")

            return result

        except Exception as e:

            logger.error(
                f"Dashboard Verification Failed: {e}"
            )

            return False

    def verify_invalid_login(self):
        """Verify Invalid Login Message"""

        try:

            logger.info(
                "Verifying Invalid Login Message"
            )

            self.wait.until(
                EC.visibility_of_element_located(
                    self.invalid_message
                )
            )

            result = (
                "auth/login"
                in self.driver.current_url
            )

            logger.info(
                "Invalid Login Verified Successfully"
            )

            return result

        except Exception as e:

            logger.error(
                f"Invalid Login Verification Failed: {e}"
            )

            return False

    def click_forgot_password(self):
        """Click Forgot Password Link"""

        try:

            logger.info(
                "Clicking Forgot Password Link"
            )

            forgot = self.wait.until(
                EC.element_to_be_clickable(
                    self.forgot_password_link
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                forgot
            )

            logger.info(
                "Forgot Password Link Clicked Successfully"
            )

        except Exception as e:

            logger.error(
                f"Forgot Password Click Failed: {e}"
            )

            raise

    def enter_forgot_username(self):
        """Enter Forgot Password Username"""

        try:

            logger.info(
                "Entering Forgot Password Username"
            )

            username_input = self.wait.until(
                EC.visibility_of_element_located(
                    self.forgot_username
                )
            )

            username_input.clear()

            username_input.send_keys("Admin")

            logger.info(
                "Forgot Password Username Entered Successfully"
            )

        except Exception as e:

            logger.error(
                f"Entering Forgot Username Failed: {e}"
            )

            raise

    def click_reset_password(self):
        """Click Reset Password Button"""

        try:

            logger.info(
                "Clicking Reset Password Button"
            )

            reset_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.reset_password_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                reset_btn
            )

            logger.info(
                "Reset Password Button Clicked Successfully"
            )

        except Exception as e:

            logger.error(
                f"Reset Password Click Failed: {e}"
            )

            raise

    def verify_reset_message(self):
        """Verify Reset Password Message"""

        try:

            logger.info(
                "Verifying Reset Password Message"
            )

            result = (
                "requestResetPassword"
                in self.driver.current_url
            )

            logger.info(
                "Reset Password Verified Successfully"
            )

            return result

        except Exception as e:

            logger.error(
                f"Reset Password Verification Failed: {e}"
            )

            return False