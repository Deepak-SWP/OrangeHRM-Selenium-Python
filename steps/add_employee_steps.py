import allure
from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.add_employee_page import EmployeePage


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@given('admin is logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@when('admin clicks PIM menu')
def step_impl(context):

    context.employee = EmployeePage(
        context.driver
    )

    context.employee.click_pim()


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@when('admin clicks Add Employee button')
def step_impl(context):

    context.employee.click_add_employee()


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@when('admin enters firstname and lastname')
def step_impl(context):

    context.employee.enter_employee_details()


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@when('admin clicks Save')
def step_impl(context):

    context.employee.click_save()


@allure.feature("PIM Module")
@allure.story("Add Employee Successfully")
@then('employee added successfully')
def step_impl(context):

    assert context.employee.verify_employee_added()

    context.driver.quit()