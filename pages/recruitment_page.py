from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class RecruitmentPage:
    """Recruitment Module Functionality"""

    recruitment_menu = (
        By.XPATH,
        "//span[text()='Recruitment']"
    )

    recruitment_text = (
        By.XPATH,
        "//h6[text()='Recruitment']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    def click_recruitment(self):
        """Click Recruitment Menu"""

        try:

            logger.info("Clicking Recruitment Menu")

            recruitment = self.wait.until(
                EC.element_to_be_clickable(
                    self.recruitment_menu
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                recruitment
            )

            logger.info("Recruitment Menu Clicked Successfully")

        except Exception as e:

            logger.error(f"Recruitment Menu Click Failed: {e}")

            raise

    def verify_recruitment_page(self):
        """Verify Recruitment Page"""

        try:

            logger.info("Verifying Recruitment Page")

            self.wait.until(
                EC.visibility_of_element_located(
                    self.recruitment_text
                )
            )

            result = (
                "recruitment"
                in self.driver.current_url.lower()
            )

            logger.info("Recruitment Page Verified Successfully")

            return result

        except Exception as e:

            logger.error(f"Recruitment Page Verification Failed: {e}")

            return False