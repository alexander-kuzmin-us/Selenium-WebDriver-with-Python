"""
A Test for logout function.
User should be able to log out.
"""
from pages.login_page import TheInternetLoginPage
from pages.secure_area_page import SecureAreaPage


def test_logout(browser):
    login_page = TheInternetLoginPage(browser)
    secure_page = SecureAreaPage(browser)
    USER_NAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    PHRASE = "Welcome to the Secure Area. When you are done click logout below."
    LOGIN_PHRASE = "Login Page"

    # Given user logged in and secure area page is displayed
    login_page.load()
    login_page.username(USER_NAME)
    login_page.password(PASSWORD)
    login_page.login_button()
    assert PHRASE == secure_page.welcome_phrase()

    # When the user click the "Logout" button
    secure_page.logout_button()

    # Then the user redirected to the login page and message "You logged out of the secure area!" appear.
    assert LOGIN_PHRASE == secure_page.login_page_phrase()