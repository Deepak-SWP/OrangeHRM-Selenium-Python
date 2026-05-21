import allure

from behave import *

from utils.driver_setup import get_driver

from utils.config import USERNAME, PASSWORD

from pages.login_page import LoginPage

from pages.recruitment_page import RecruitmentPage

from utils.logger import logger


@allure.feature("Recruitment Module")
@allure.story("Open Recruitment Module")
@given('admin logged into recruitment page')
def step_impl(context):
    """Login to OrangeHRM Application"""

    logger.info("Launching Browser")

    context.driver = get_driver()

    login = LoginPage(
        context.driver
    )

    login.open()

    login.login(USERNAME, PASSWORD)

    context.recruitment = RecruitmentPage(
        context.driver
    )


@when('admin clicks Recruitment menu')
def step_impl(context):
    """Click Recruitment Menu"""

    context.recruitment.click_recruitment()


@then('recruitment page should display')
def step_impl(context):
    """Verify Recruitment Page"""

    assert context.recruitment.verify_recruitment_page()

    logger.info("Recruitment Page Verified Successfully")

    context.driver.quit()

    logger.info("Browser Closed Successfully")