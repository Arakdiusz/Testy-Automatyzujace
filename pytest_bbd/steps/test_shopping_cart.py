from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Constants
SAUCE_DEMO_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def browser():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@scenario('add_remove_cart.feature', 'User can add and remove items from the cart after logging in')
def test_add_and_remove_from_cart():
    pass


@given('the user has logged in to the "saucedemo" website')
def login(browser):
    browser.get(SAUCE_DEMO_URL)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys(USERNAME)
    wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
    assert "inventory" in browser.current_url


@when('the user adds an item to the cart')
def add_item_to_cart(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_inventory'))).click()


@when('the user removes the item from the cart')
def remove_item_from_cart(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_secondary'))).click()


@then('the cart should be empty')
def cart_is_empty(browser):
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    cart_items = browser.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(cart_items) == 0
