from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no 'login' word in url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is no register form"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_FORM)
        email_form.send_keys(email)
        password1_form = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION_FORM)
        password1_form.send_keys(password)
        password2_form = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION_FORM)
        password2_form.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
