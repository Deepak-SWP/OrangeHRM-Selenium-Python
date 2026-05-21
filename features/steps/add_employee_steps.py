import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.add_employee_page import EmployeePage

from utils.logger import logger


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@given('admin is logged into OrangeHRM')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    context.employee = EmployeePage(
        context.driver
    )


@when('admin clicks PIM menu')
def step_impl(context):
    """Click PIM Menu"""

    context.employee.click_pim()


@when('admin clicks Add Employee button')
def step_impl(context):
    """Click Add Employee Button"""

    context.employee.click_add_employee()


@when('admin enters firstname and lastname')
def step_impl(context):
    """Enter Employee Details"""

    context.employee.enter_employee_details()


@when('admin clicks Save')
def step_impl(context):
    """Click Save Button"""

    context.employee.click_save()


@then('employee added successfully')
def step_impl(context):
    """Verify Employee Added Successfully"""

    assert context.employee.verify_employee_added()

    logger.info("Employee Added Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")