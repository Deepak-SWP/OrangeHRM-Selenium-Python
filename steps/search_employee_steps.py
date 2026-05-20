import allure
from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.search_employee_page import SearchEmployeePage


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@given('admin logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@when('admin opens PIM module')
def step_impl(context):

    context.search = SearchEmployeePage(
        context.driver
    )

    context.search.click_pim()


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@when('admin searches employee name')
def step_impl(context):

    context.search.search_employee()


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@when('admin clicks search button')
def step_impl(context):

    context.search.click_search()


@allure.feature("PIM Module")
@allure.story("Search Added Employee")
@then('employee details should display')
def step_impl(context):

    assert context.search.verify_employee()

    context.driver.quit()