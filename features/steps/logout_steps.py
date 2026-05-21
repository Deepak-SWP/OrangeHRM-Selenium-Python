import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage

from utils.logger import logger


@allure.feature("Logout Module")
@allure.story("Logout Successfully")
@given('user logged into OrangeHRM')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    context.dashboard = DashboardPage(
        context.driver
    )


@when('user clicks profile menu')
def step_impl(context):
    """Click Profile Menu"""

    context.dashboard.click_profile()


@when('user clicks logout option')
def step_impl(context):
    """Click Logout Option"""

    context.dashboard.click_logout()


@then('login page should display')
def step_impl(context):
    """Verify Login Page"""

    assert context.dashboard.verify_login_page()

    logger.info("Login Page Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")