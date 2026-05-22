import allure

from behave import given, when, then

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.employee_list_page import EmployeeListPage

from utils.logger import logger


@allure.feature("PIM Module")
@allure.story("View Employee List")
@given('admin logged into OrangeHRM for employee list')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    context.employee = EmployeeListPage(
        context.driver
    )


@when('admin clicks PIM menu for employee list')
def step_impl(context):
    """Click PIM Menu"""

    context.employee.click_pim()


@when('admin opens employee list page')
def step_impl(context):
    """Open Employee List Page"""

    context.employee.open_employee_list()


@then('employee records should display successfully')
def step_impl(context):
    """Verify Employee Records"""

    assert context.employee.verify_employee_records()

   

    context.driver.quit()

    logger.info("Browser Closed Successfully")