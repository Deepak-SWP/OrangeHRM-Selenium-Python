from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.update_employee_page import UpdateEmployeePage


@given('admin logged into OrangeHRM system')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)


@when('admin opens PIM module for update')
def step_impl(context):

    context.update = UpdateEmployeePage(
        context.driver
    )

    context.update.click_pim()


@when('admin opens employee record')
def step_impl(context):

    context.update.open_employee_record()


@when('admin updates employee details')
def step_impl(context):

    context.update.update_employee_details()


@when('admin clicks save button')
def step_impl(context):

    context.update.click_save()


@then('employee details should update successfully')
def step_impl(context):

    assert context.update.verify_update()

    context.driver.quit()