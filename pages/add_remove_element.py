"""
this module contains the page object for add_remove_element page
"""
from selenium.webdriver.common.by import By


class AddRemoveElementPage:
    # URL
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    # Locators
    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add Element')]")
    DELETE_BUTTON = (By.CLASS_NAME, 'added-manually')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    def load(self):
        self.browser.get(self.URL)

    def add_element_button(self):
        add_button = self.browser.find_element(*self.ADD_BUTTON)
        add_button.click()

    def delete_button_text(self):
        button = self.browser.find_element(*self.DELETE_BUTTON)
        text = button.text
        return text
