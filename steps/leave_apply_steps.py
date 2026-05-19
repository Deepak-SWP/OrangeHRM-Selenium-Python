from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.leave_page import LeavePage


@given('employee logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)


@when('employee clicks Leave menu')
def step_impl(context):

    context.leave = LeavePage(
        context.driver
    )

    context.leave.click_leave_menu()


@then('leave page should display')
def step_impl(context):

    assert context.leave.verify_leave_page()

    context.driver.quit()