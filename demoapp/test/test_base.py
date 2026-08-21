import pytest

@pytest.fixture
def selenium_driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()