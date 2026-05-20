import allure
from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage


@allure.feature("Login Module")
@allure.story("Invalid Login Validation")
@given('user opens OrangeHRM login page')
def step_impl(context):

    context.driver = get_driver()

    context.login = LoginPage(
        context.driver
    )

    context.login.open()


@allure.feature("Login Module")
@allure.story("Invalid Login Validation")
@when('user enters invalid username and password')
def step_impl(context):

    context.login.login(
        "Admin123",
        "wrongpass"
    )


@allure.feature("Login Module")
@allure.story("Invalid Login Validation")
@when('user clicks login button')
def step_impl(context):

    pass


@allure.feature("Login Module")
@allure.story("Invalid Login Validation")
@then('invalid credentials message should display')
def step_impl(context):

    assert context.login.verify_invalid_login()

    context.driver.quit()