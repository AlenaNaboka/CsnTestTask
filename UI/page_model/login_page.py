from UI.locators.login_page import LoginPageLocators
from UI.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        return 'https://login.' + super(LoginPage, self).url

    @property
    def username_field(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
