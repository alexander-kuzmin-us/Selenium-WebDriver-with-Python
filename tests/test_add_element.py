"""
User should be able to add element
"""
from pages.add_remove_element import AddRemoveElementPage


def test_add_element(browser):
    TEXT = "Delete"
    add_element_page = AddRemoveElementPage(browser)

    # Given the add_element page is displayed.
    add_element_page.load()

    # When user click the "Add Element" button.
    add_element_page.add_element_button()

    # Then the "Delete" button is displayed.
    assert add_element_page.delete_button_text() == TEXT
