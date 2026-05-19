from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.search_user_page import SearchUserPage


@given('admin logged into OrangeHRM application')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)


@when('admin clicks Admin menu')
def step_impl(context):

    context.search = SearchUserPage(
        context.driver
    )

    context.search.click_admin()


@when('admin enters username in search')
def step_impl(context):

    context.search.enter_username()


@when('admin clicks user search button')
def step_impl(context):

    context.search.click_search()


@then('user records should display')
def step_impl(context):

    assert context.search.verify_records()

    context.driver.quit()