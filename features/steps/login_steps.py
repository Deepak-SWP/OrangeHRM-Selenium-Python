import csv

import allure

from behave import *

from utils.driver_setup import get_driver

from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage

from utils.logger import logger


@allure.feature("Login Module")
@allure.story("Valid Login with DDT")
@given('user is on login page')
def step_impl(context):
    """Open OrangeHRM Login Page"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    context.login = LoginPage(context.driver)

    context.login.open()


@when('user enters valid username and password')
def step_impl(context):
    """Perform Login using CSV Data"""

    logger.info("Reading Login Data from CSV")

    with open("testdata/login_data.csv", newline='') as file:

        data = csv.DictReader(file)

        for row in data:

            username = row["username"]

            password = row["password"]

            logger.info(
                f"Trying Login with Username: {username}"
            )

            context.login.login(
                username,
                password
            )


@when('clicks login button')
def step_impl(context):
    """Login Button Clicked"""

    pass


@then('user should navigate to dashboard')
def step_impl(context):
    """Verify Dashboard Navigation"""

    dashboard = DashboardPage(
        context.driver
    )

    assert dashboard.verify_dashboard()

    logger.info("Dashboard Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")