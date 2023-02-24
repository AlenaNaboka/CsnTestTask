from selenium.webdriver.common.by import By


# describe the elements which are available on login page
class LoginPageLocators:
    # FIELDS
    USERNAME_FIELD = By.ID, "login-username"
    PASSWORD_FIELD = By.ID, "login-passwd"
    # BUTTONS
    SIGN_IN_BUTTON = By.ID, "login-signin"
