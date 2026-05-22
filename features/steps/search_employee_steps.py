import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.search_employee_page import SearchEmployeePage

from utils.logger import logger


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@given('admin logged into OrangeHRM')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    context.search = SearchEmployeePage(
        context.driver
    )


@when('admin opens PIM module')
def step_impl(context):
    """Open PIM Module"""

    context.search.click_pim()


@when('admin searches employee name')
def step_impl(context):
    """Search Employee Name"""

    context.search.search_employee()


@when('admin clicks search button')
def step_impl(context):
    """Click Search Button"""

    context.search.click_search()


@then('employee details should display')
def step_impl(context):
    """Verify Employee Details"""

    assert context.search.verify_employee()


    context.driver.quit()

    logger.info("Browser Closed Successfully")