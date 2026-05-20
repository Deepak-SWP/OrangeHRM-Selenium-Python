import allure
from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.recruitment_page import RecruitmentPage


@allure.feature("Recruitment Module")
@allure.story("Open Recruitment Module")
@given('admin logged into recruitment page')
def step_impl(context):

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)


@when('admin clicks Recruitment menu')
def step_impl(context):

    context.recruitment = RecruitmentPage(
        context.driver
    )

    context.recruitment.click_recruitment()



@then('recruitment page should display')
def step_impl(context):

    assert context.recruitment.verify_recruitment_page()

    context.driver.quit()