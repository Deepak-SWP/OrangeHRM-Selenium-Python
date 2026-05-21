import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.leave_page import LeavePage

from utils.logger import logger


@allure.feature("Leave Module")
@allure.story("Open Leave Page")
@given('employee logged into OrangeHRM')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.leave = LeavePage(
        context.driver
    )


@when('employee clicks Leave menu')
def step_impl(context):
    """Click Leave Menu"""

    context.leave.click_leave_menu()


@then('leave page should display')
def step_impl(context):
    """Verify Leave Page"""

    assert context.leave.verify_leave_page()

    logger.info("Leave Page Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")