import allure
from behave import *

from utils.driver_setup import get_driver
from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Dashboard Module")
@allure.story("Verify Dashboard Page")
@given('admin successfully logged into OrangeHRM')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.dashboard = DashboardPage(
        context.driver
    )



@then('dashboard page should be displayed')
def step_impl(context):

    assert context.dashboard.verify_dashboard()

    context.driver.quit()