from selenium.webdriver.common.by import By


# describe the elements which are available on finance page
class FinancePageLocators:
    # BUTTONS
    MARKET_DATA_TAB = By.CSS_SELECTOR, "div[title='Market Data']"
    # POPUP OPTIONS
    CALENDAR_OPTION = By.CSS_SELECTOR, "a[title='Calendar']"
