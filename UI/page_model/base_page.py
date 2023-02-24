from UI.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'yahoo.com'

    @property
    def sign_in_button(self):
        return self.driver.find_element(*BasePageLocators.SIGN_IN_BUTTON)

    @property
    def consent_form(self):
        return self.driver.find_element(*BasePageLocators.CONSENT_FORM)

    @property
    def accept_button(self):
        return self.driver.find_element(*BasePageLocators.ACCEPT_BUTTON)

    @property
    def finance_tab(self):
        return self.driver.find_element(*BasePageLocators.FINANCE_TAB)
