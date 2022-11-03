import pytest
from pages.login_page import LoginPage

link = 'https://www.saucedemo.com/'


def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_form()
