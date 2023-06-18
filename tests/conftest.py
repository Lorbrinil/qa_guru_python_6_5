import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.driver.set_window_size(1920, 1080)

    yield

    browser.quit()