from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class SearchUserPage:
    """Search User Functionality"""

    admin_menu = (
        By.XPATH,
        "//a[contains(@href,'admin/viewAdminModule')]"
    )

    username_field = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    search_button = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    records_found = (
        By.XPATH,
        "//div[@class='oxd-table-card']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_admin(self):
        """Click Admin Menu"""

        try:

            logger.info("Clicking Admin Menu")

            admin = self.wait.until(
                EC.element_to_be_clickable(
                    self.admin_menu
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                admin
            )

            logger.info("Admin Menu Clicked Successfully")

        except Exception as e:

            logger.error(f"Admin Menu Click Failed: {e}")

            raise

    def enter_username(self):
        """Enter Username for Search"""

        try:

            logger.info("Entering Username")

            field = self.wait.until(
                EC.visibility_of_element_located(
                    self.username_field
                )
            )

            field.clear()

            field.send_keys("Admin")

            logger.info("Username Entered Successfully")

        except Exception as e:

            logger.error(f"Username Entry Failed: {e}")

            raise

    def click_search(self):
        """Click Search Button"""

        try:

            logger.info("Clicking Search Button")

            search_btn = self.wait.until(
                EC.element_to_be_clickable(
                    self.search_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                search_btn
            )

            logger.info("Search Button Clicked Successfully")

        except Exception as e:

            logger.error(f"Search Button Click Failed: {e}")

            raise

    def verify_records(self):
        """Verify User Records"""

        try:

            logger.info("Verifying User Records")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.records_found
                )
            )

            rows = self.driver.find_elements(
                By.XPATH,
                "//div[@class='oxd-table-card']"
            )

            result = (
                len(rows) > 0
                and
                "viewSystemUsers"
                in self.driver.current_url
            )

            logger.info("User Records Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"User Records Verification Failed: {e}")

            return False