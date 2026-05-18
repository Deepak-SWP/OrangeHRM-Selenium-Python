from behave import *
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD


@given('user is on login page')
def step_impl(context):
    context.driver = get_driver()
    context.login = LoginPage(context.driver)
    context.login.open()


@when('user enters valid username and password')
def step_impl(context):
    context.login.login(USERNAME, PASSWORD)


@when('clicks login button')
def step_impl(context):
    pass


@then('user should navigate to dashboard')
def step_impl(context):
    dashboard = DashboardPage(context.driver)
    assert dashboard.verify_dashboard()
    context.driver.quit()