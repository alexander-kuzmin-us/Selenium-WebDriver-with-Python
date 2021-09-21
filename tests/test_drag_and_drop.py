"""
A Test Drag and Drop page.
User should be able to drag the "Box A" and drop it to the "Box B".
"""

from pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop(browser):
    page = DragAndDropPage(browser)

    # Given Drag and Drop page is displayed
    page.load()

    # When user drag the element "Box A" and drop it to the element "Box B"
    page.action()