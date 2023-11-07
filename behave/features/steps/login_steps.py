from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The saucedemo login page is open')
def open_saucedemo_login_page(context):
    context.browser.get("https://www.saucedemo.com")


@when('I enter username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, 'user-name'))
    ).send_keys(username)
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    ).send_keys(password)
    context.browser.find_element(By.ID, 'login-button').click()


@then('I should see an error message "{error_message}"')
def verify_error_message(context, error_message):
    error = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    ).text
    assert error_message in error
