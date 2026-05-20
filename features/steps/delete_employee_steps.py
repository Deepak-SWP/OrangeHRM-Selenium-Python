import allure
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.delete_employee_page import DeleteEmployeePage


@allure.feature("PIM Module")
@allure.story("Delete Employee Record")
@given('admin logged into OrangeHRM portal')
def step_impl(context):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    context.driver = driver

    context.delete = DeleteEmployeePage(driver)

    context.delete.wait.until(
        lambda d: d.find_element("name", "username")
    ).send_keys("Admin")

    context.driver.find_element(
        "name",
        "password"
    ).send_keys("admin123")

    context.driver.find_element(
        "xpath",
        "//button[@type='submit']"
    ).click()



@when('admin opens PIM module for delete')
def step_impl(context):

    context.delete.open_pim()
    context.delete.open_employee_list()


@when('admin selects employee record')
def step_impl(context):

    context.delete.select_employee_record()



@when('admin clicks delete button')
def step_impl(context):

    context.delete.click_delete_button()



@when('admin confirms delete action')
def step_impl(context):

    context.delete.confirm_delete_action()



@then('employee record should delete successfully')
def step_impl(context):

    assert context.delete.verify_delete_success()

    context.driver.quit()