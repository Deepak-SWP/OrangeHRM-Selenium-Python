import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.search_user_page import SearchUserPage

from utils.logger import logger


@allure.feature("Admin Module")
@allure.story("Search User Records")
@given('admin logged into OrangeHRM application')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.search = SearchUserPage(
        context.driver
    )


@when('admin clicks Admin menu')
def step_impl(context):
    """Click Admin Menu"""

    context.search.click_admin()


@when('admin enters username in search')
def step_impl(context):
    """Enter Username for Search"""

    context.search.enter_username()


@when('admin clicks user search button')
def step_impl(context):
    """Click User Search Button"""

    context.search.click_search()


@then('user records should display')
def step_impl(context):
    """Verify User Records"""

    assert context.search.verify_records()

    logger.info("User Records Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")