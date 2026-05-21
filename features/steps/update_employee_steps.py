import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.update_employee_page import UpdateEmployeePage

from utils.logger import logger


@allure.feature("PIM Module")
@allure.story("Update Employee Details")
@given('admin logged into OrangeHRM system')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.update = UpdateEmployeePage(
        context.driver
    )


@when('admin opens PIM module for update')
def step_impl(context):
    """Open PIM Module"""

    context.update.click_pim()


@when('admin opens employee record')
def step_impl(context):
    """Open Employee Record"""

    context.update.open_employee_record()


@when('admin updates employee details')
def step_impl(context):
    """Update Employee Details"""

    context.update.update_employee_details()


@when('admin clicks save button')
def step_impl(context):
    """Click Save Button"""

    context.update.click_save()


@then('employee details should update successfully')
def step_impl(context):
    """Verify Employee Update"""

    assert context.update.verify_update()

    logger.info("Employee Updated Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")