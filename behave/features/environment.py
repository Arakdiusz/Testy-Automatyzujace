from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def before_all(context):
    service = Service(executable_path=r'features/chromedriver.exe')

    context.browser = webdriver.Chrome(service=service)


def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
