from selenium.webdriver.common.by import By


# describe the elements which are available on calendar page
def get_market_data(date, month):
    return By.XPATH, f'//span[text()="{date}"]/following-sibling::span//span[text()="{month}"]' \
                     f'//ancestor::li/child::a'


def get_expected_date_locator(date, month):
    return By.XPATH, f'//span[text()="{date}"]/following-sibling::span//span[text()="{month}"]'


class CalendarPageLocators:
    # FORMS
    CALENDAR_FORM = By.ID, "fin-cal-events"
    # BUTTONS
    PREV_DATE_BUTTON = By.CSS_SELECTOR, "a[title=Prev]"
    NEXT_DATE_BUTTON = By.CSS_SELECTOR, "a[title=Next]"
