"""
This module contains DragAndDropPage,
the page object for The Internet "Drag and Drop page".
"""
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragAndDropPage:

    # URL
    URL = "https://the-internet.herokuapp.com/drag_and_drop"

    # Locators
    SOURCE = (By.XPATH, "//div[@id='column-a']")
    TARGET = (By.XPATH, "//div[@id='column-b']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def action(self):
        action = ActionChains(self.browser)
        source = self.browser.find_element(*self.SOURCE)
        target = self.browser.find_element(*self.TARGET)
        action.drag_and_drop(source, target).perform()
