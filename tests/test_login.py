"""
A Test for login page with valid credentials.
User should be able to login with valid credentials.
"""

from pages.login_page import TheInternetLoginPage
from pages.secure_area_page import SecureAreaPage


def test_login(browser):
    login_page = TheInternetLoginPage(browser)
    secure_page = SecureAreaPage(browser)
    USER_NAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    PHRASE = "Welcome to the Secure Area. When you are done click logout below."

    # Given the Login Page is displayed
    login_page.load()

    # When the User type “tomsmith” into the Username field
    login_page.username(USER_NAME)

    # And the User type “SuperSecretPassword!” Into the Password field
    login_page.password(PASSWORD)

    # And user click the Login button
    login_page.login_button()

    # Then User logged in to secure area
    assert PHRASE == secure_page.welcome_phrase()
