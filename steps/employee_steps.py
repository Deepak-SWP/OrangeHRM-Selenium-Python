from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.employee_page import EmployeePage


@given('admin is logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)


@when('admin clicks PIM menu')
def step_impl(context):

    context.employee = EmployeePage(
        context.driver
    )

    context.employee.click_pim()


@when('admin clicks Add Employee button')
def step_impl(context):

    context.employee.click_add_employee()


@when('admin enters firstname and lastname')
def step_impl(context):

    context.employee.enter_employee_details()


@when('admin clicks Save')
def step_impl(context):

    context.employee.click_save()


@then('employee added successfully')
def step_impl(context):

    assert context.employee.verify_employee_added()

    context.driver.quit()