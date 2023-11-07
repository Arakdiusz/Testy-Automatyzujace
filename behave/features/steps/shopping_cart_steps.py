from selenium.webdriver.common.by import By
from behave import given, when, then


def scroll_to_top(context):
    context.browser.execute_script("window.scrollTo(0, 0);")


@given('I am logged in with valid credentials')
def step_impl(context):
    context.browser.get('https://www.saucedemo.com/')
    context.browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.browser.find_element(By.ID, 'login-button').click()


@when('I add a single item to the cart')
def step_impl(context):
    scroll_to_top(context)
    add_button = context.browser.find_elements(By.CLASS_NAME, 'btn_inventory')[0]
    add_button.click()


@then('the cart should display one item')
def step_impl(context):
    cart_badge = context.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '1'


@when('I add multiple items to the cart')
def step_impl(context):
    scroll_to_top(context)
    add_buttons = context.browser.find_elements(By.CLASS_NAME, 'btn_inventory')
    for button in add_buttons:
        button.click()
    context.items_added = len(add_buttons)


@then('the cart should display the correct number of items')
def step_impl(context):
    cart_badge = context.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == str(context.items_added)


@given('I have items in my shopping cart')
def step_impl(context):
    scroll_to_top(context)
    context.execute_steps(u'''
        Given I am logged in with valid credentials
        When I add multiple items to the cart
    ''')
    scroll_to_top(context)


@when('I remove an item from the cart')
def step_impl(context):
    scroll_to_top(context)
    context.browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    remove_buttons = context.browser.find_elements(By.CLASS_NAME, 'cart_button')
    remove_buttons[0].click()
    context.items_added -= 1
