import allure
from behave import *

from utils.driver_setup import get_driver
from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Logout Module")
@allure.story("Logout Successfully")
@given('user logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(context.driver)

    login.open()

    login.login(USERNAME, PASSWORD)


@allure.feature("Logout Module")
@allure.story("Logout Successfully")
@when('user clicks profile menu')
def step_impl(context):

    context.dashboard = DashboardPage(
        context.driver
    )

    context.dashboard.click_profile()


@allure.feature("Logout Module")
@allure.story("Logout Successfully")
@when('user clicks logout option')
def step_impl(context):

    context.dashboard.click_logout()


@allure.feature("Logout Module")
@allure.story("Logout Successfully")
@then('login page should display')
def step_impl(context):

    assert context.dashboard.verify_login_page()

    context.driver.quit()