from selenium.webdriver.common.by import By


# describe the elements which are available on all pages
class BasePageLocators:
    # BUTTONS
    SIGN_IN_BUTTON = By.ID, "ybarAccountProfile"
    ACCEPT_BUTTON = By.CSS_SELECTOR, "button[name=agree]"
    # TABS
    FINANCE_TAB = By.ID, 'root_7'
    # FORM
    CONSENT_FORM = By.CLASS_NAME, "consent-form"
