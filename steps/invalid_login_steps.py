from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage


@given('user opens OrangeHRM login page')
def step_impl(context):

    context.driver = get_driver()

    context.login = LoginPage(
        context.driver
    )

    context.login.open()


@when('user enters invalid username and password')
def step_impl(context):

    context.login.login(
        "Admin123",
        "wrongpass"
    )


@when('user clicks login button')
def step_impl(context):

    pass


@then('invalid credentials message should display')
def step_impl(context):

    assert context.login.verify_invalid_login()

    context.driver.quit()