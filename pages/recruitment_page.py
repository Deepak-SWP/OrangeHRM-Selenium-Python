from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class RecruitmentPage:

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

        self.wait.until(
            EC.element_to_be_clickable(
                self.recruitment_menu
            )
        ).click()

    def verify_recruitment_page(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.recruitment_text
            )
        ).is_displayed()