import allure
from behave import given, when, then

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.leave_search_page import LeaveSearchPage


@allure.feature("Leave Module")
@allure.story("Search Leave Records")
@given('admin logged into OrangeHRM for leave search')
def step_impl(context):

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    context.driver = driver

    context.leave = LeaveSearchPage(driver)

    context.leave.wait.until(
        lambda d: d.find_element(
            "name",
            "username"
        )
    ).send_keys("Admin")

    context.driver.find_element(
        "name",
        "password"
    ).send_keys("admin123")

    context.driver.find_element(
        "xpath",
        "//button[@type='submit']"
    ).click()


@allure.feature("Leave Module")
@allure.story("Search Leave Records")
@when('admin clicks Leave menu')
def step_impl(context):

    context.leave.click_leave()


@allure.feature("Leave Module")
@allure.story("Search Leave Records")
@when('admin searches leave records')
def step_impl(context):

    context.leave.search_leave_records()


@allure.feature("Leave Module")
@allure.story("Search Leave Records")
@then('leave records should display successfully')
def step_impl(context):

    assert context.leave.verify_leave_records()

    context.driver.quit()