from UI.locators.finance_page import FinancePageLocators
from UI.page_model.base_page import BasePage


class FinancePage(BasePage):
    @property
    def url(self):
        return 'https://finance.' + super(FinancePage, self).url

    @property
    def market_data_tab(self):
        return self.driver.find_element(*FinancePageLocators.MARKET_DATA_TAB)

    @property
    def calendar_option(self):
        return self.driver.find_element(*FinancePageLocators.CALENDAR_OPTION)
