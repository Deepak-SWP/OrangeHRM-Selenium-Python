import allure
from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.employee_list_page import EmployeeListPage


@allure.feature("PIM Module")
@allure.story("View Employee List")
@given('admin logged into OrangeHRM for employee list')
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

    context.employee = EmployeeListPage(driver)

    context.employee.wait.until(
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


@when('admin clicks PIM menu for employee list')
def step_impl(context):

    context.employee.click_pim()



@when('admin opens employee list page')
def step_impl(context):

    context.employee.open_employee_list()



@then('employee records should display successfully')
def step_impl(context):

    assert context.employee.verify_employee_records()

    context.driver.quit()