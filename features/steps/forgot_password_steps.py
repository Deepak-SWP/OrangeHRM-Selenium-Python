import allure

from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage

from utils.logger import logger


@allure.feature("Forgot Password Module")
@allure.story("Reset Password Successfully")
@given('user is on OrangeHRM login page')
def step_impl(context):
    """Open OrangeHRM Login Page"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    context.login = LoginPage(
        context.driver
    )

    context.login.open()


@when('user clicks forgot password link')
def step_impl(context):
    """Click Forgot Password Link"""

    context.login.click_forgot_password()


@when('user enters username')
def step_impl(context):
    """Enter Username for Password Reset"""

    context.login.enter_forgot_username()


@when('user clicks reset password button')
def step_impl(context):
    """Click Reset Password Button"""

    context.login.click_reset_password()


@then('reset password message should display')
def step_impl(context):
    """Verify Reset Password Message"""

    assert context.login.verify_reset_message()

    logger.info("Reset Password Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")