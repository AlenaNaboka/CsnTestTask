from UI.locators.calendar_page import CalendarPageLocators, get_market_data, get_expected_date_locator
from UI.page_model.finance_page import FinancePage


class CalendarPage(FinancePage):
    def __init__(self, driver, day, month):
        super(FinancePage, self).__init__(driver)
        # self.driver = driver
        self.day = day
        self.month = month

    @property
    def url(self):
        return 'https://finance.' + super(CalendarPage, self).url

    @property
    def calendar_form(self):
        return self.driver.find_element(*CalendarPageLocators.CALENDAR_FORM)

    @property
    def prev_date_button(self):
        return self.driver.find_element(*CalendarPageLocators.PREV_DATE_BUTTON)

    @property
    def next_date_button(self):
        return self.driver.find_element(*CalendarPageLocators.NEXT_DATE_BUTTON)

    def get_day_market_data(self):
        return self.driver.find_elements(*get_market_data(self.day, self.month))

    def get_specific_day_locator(self):
        return self.driver.find_elements(*get_expected_date_locator(self.day, self.month))
