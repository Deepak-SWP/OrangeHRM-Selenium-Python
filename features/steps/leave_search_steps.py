import allure

from behave import given, when, then

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.leave_search_page import LeaveSearchPage

from utils.logger import logger


@allure.feature("Leave Module")
@allure.story("Search Leave Records")
@given('admin logged into OrangeHRM for leave search')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    context.leave = LeaveSearchPage(
        context.driver
    )


@when('admin clicks Leave menu')
def step_impl(context):
    """Click Leave Menu"""

    context.leave.click_leave()


@when('admin searches leave records')
def step_impl(context):
    """Search Leave Records"""

    context.leave.search_leave_records()


@then('leave records should display successfully')
def step_impl(context):
    """Verify Leave Records"""

    assert context.leave.verify_leave_records()

    

    context.driver.quit()

    logger.info("Browser Closed Successfully")