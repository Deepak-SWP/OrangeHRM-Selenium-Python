import allure

from behave import given, when, then

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.delete_employee_page import DeleteEmployeePage

from utils.logger import logger


@allure.feature("PIM Module")
@allure.story("Delete Employee Record")
@given('admin logged into OrangeHRM portal')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)

    logger.info("Login Successful")

    context.delete = DeleteEmployeePage(
        context.driver
    )


@when('admin opens PIM module for delete')
def step_impl(context):
    """Open PIM Module and Employee List"""

    context.delete.open_pim()

    context.delete.open_employee_list()


@when('admin selects employee record')
def step_impl(context):
    """Select Employee Record"""

    context.delete.select_employee_record()


@when('admin clicks delete button')
def step_impl(context):
    """Click Delete Button"""

    context.delete.click_delete_button()


@when('admin confirms delete action')
def step_impl(context):
    """Confirm Delete Action"""

    context.delete.confirm_delete_action()


@then('employee record should delete successfully')
def step_impl(context):
    """Verify Employee Delete Success"""

    assert context.delete.verify_delete_success()

    

    context.driver.quit()

    logger.info("Browser Closed Successfully")