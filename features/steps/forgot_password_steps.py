import allure
from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage


@allure.feature("Forgot Password Module")
@allure.story("Reset Password Successfully")
@given('user is on OrangeHRM login page')
def step_impl(context):

    context.driver = get_driver()

    context.login = LoginPage(
        context.driver
    )

    context.login.open()



@when('user clicks forgot password link')
def step_impl(context):

    context.login.click_forgot_password()



@when('user enters username')
def step_impl(context):

    context.login.enter_forgot_username()



@when('user clicks reset password button')
def step_impl(context):

    context.login.click_reset_password()



@then('reset password message should display')
def step_impl(context):

    assert context.login.verify_reset_message()

    context.driver.quit()