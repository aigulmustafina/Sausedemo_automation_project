from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)
