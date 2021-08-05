"""
This module contains TheInternetLoginPage,
the page object for The Internet Login page.
"""
from selenium.webdriver.common.by import By


class TheInternetLoginPage:

    # URL
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USER_NAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    BUTTON = (By.XPATH, "//i[contains(text(),'Login')]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def username(self, username):
        username_input = self.browser.find_element(*self.USER_NAME_INPUT)
        username_input.send_keys(username)

    def password(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def login_button(self):
        button_click = self.browser.find_element(*self.BUTTON)
        button_click.click()

