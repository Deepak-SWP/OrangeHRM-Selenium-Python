from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import URL


class LoginPage:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL)

    def login(self, uname, pwd):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(uname)

        self.driver.find_element(*self.password).send_keys(pwd)

        self.driver.find_element(*self.login_btn).click()