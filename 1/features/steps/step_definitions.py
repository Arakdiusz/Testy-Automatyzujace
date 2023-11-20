
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('I open Sauce Demo homepage')
def step_open_homepage(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter wrong username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()


@then('I should see the error message "{error_message}"')
def step_verify_login(context, error_message):
    try:
        actual_error_message = context.driver.find_element(By.XPATH,
                                                           "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]").text
        assert error_message in actual_error_message
    finally:
        context.driver.quit()


@when('I enter correct username and password')
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()


@then('The title should be "{title}"')
def step_verify_title(context, title):
    assert title == context.driver.title
    context.driver.quit()


@when('I enter username and password')
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()


@then('I should be able to add an item to the cart')
def step_add_item_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
    cart_count = context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert cart_count == "1"


@then('I should be able to open the cart')
def step_impl(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_icon.click()


@then('I should be able to remove the item from the cart')
def step_impl(context):
    remove_button = context.driver.find_element(By.CSS_SELECTOR, '.cart_button')
    remove_button.click()
    context.driver.quit()
