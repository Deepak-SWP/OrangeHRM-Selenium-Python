import allure

from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage

from utils.logger import logger


@allure.feature("Login Module")
@allure.story("Invalid Login Validation")
@given('user opens OrangeHRM login page')
def step_impl(context):
    """Open OrangeHRM Login Page"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    context.login = LoginPage(
        context.driver
    )

    context.login.open()


@when('user enters invalid username and password')
def step_impl(context):
    """Enter Invalid Username and Password"""

    context.login.login(
        "Admin123",
        "wrongpass"
    )


@when('user clicks login button')
def step_impl(context):
    """Login Button Clicked"""

    pass


@then('invalid credentials message should display')
def step_impl(context):
    """Verify Invalid Login Message"""

    assert context.login.verify_invalid_login()

    logger.info("Invalid Login Message Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")