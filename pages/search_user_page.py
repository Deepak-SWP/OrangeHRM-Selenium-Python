from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class SearchUserPage:

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

        self.wait.until(
            EC.element_to_be_clickable(
                self.admin_menu
            )
        ).click()

    def enter_username(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.username_field
            )
        )

        field.clear()

        field.send_keys("Admin")

    def click_search(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.search_button
            )
        ).click()

    def verify_records(self):

        rows = self.wait.until(
            EC.presence_of_all_elements_located(
                self.records_found
            )
        )

        return len(rows) > 0