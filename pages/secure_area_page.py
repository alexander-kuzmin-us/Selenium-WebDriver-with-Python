"""
This module contains SecureAreaPage,
the page object for the Login page happy path result.
"""
from selenium.webdriver.common.by import By


class SecureAreaPage:

    # Locators
    WELCOME_PHRASE = (By.XPATH, "//h4[contains(text(),'Welcome to the Secure Area. When you are done clic')]")
    LOGIN_PAGE = (By.XPATH, "//h2[contains(text(),'Login Page')]")
    LOGOUT_BUTTON = (By.XPATH, "//i[contains(text(),'Logout')]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def welcome_phrase(self):
        page_phrase = self.browser.find_element(*self.WELCOME_PHRASE)
        text = page_phrase.text
        return text

    def logout_button(self):
        button = self.browser.find_element(*self.LOGOUT_BUTTON)
        button.click()

    def login_page_phrase(self):
        phrase = self.browser.find_element(*self.LOGIN_PAGE)
        text = phrase.text
        return text