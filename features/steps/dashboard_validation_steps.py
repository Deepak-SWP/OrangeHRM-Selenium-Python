import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage

from utils.logger import logger


@allure.feature("Dashboard Module")
@allure.story("Verify Dashboard Page")
@given('admin successfully logged into OrangeHRM')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.dashboard = DashboardPage(
        context.driver
    )


@then('dashboard page should be displayed')
def step_impl(context):
    """Verify Dashboard Page"""

    assert context.dashboard.verify_dashboard()

    

    context.driver.quit()

    logger.info("Browser Closed Successfully")