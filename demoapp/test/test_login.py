from selenium.webdriver.common.by import By

from test_base import selenium_driver

def test_login_page(selenium_driver):
    selenium_driver.get("http://localhost:5000/login")
    username_field = selenium_driver.find_element(By.ID, "username")
    password_field = selenium_driver.find_element(By.ID, "pwd")
    login_button = selenium_driver.find_element(By.ID, "login-button")

    username_field.send_keys("1")
    password_field.send_keys("1")
    login_button.click()

    selenium_driver.implicitly_wait(5)

    welcome_message = selenium_driver.find_element(By.ID, "welcome-message")
    assert selenium_driver.current_url == "http://localhost:5000/"
    assert welcome_message.text == "Hello, 1! You are logged in."
