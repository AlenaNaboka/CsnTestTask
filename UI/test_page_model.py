from selenium import webdriver
import re
from helper import username, password
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from UI.page_model.login_page import LoginPage
from UI.page_model.base_page import BasePage
from UI.page_model.finance_page import FinancePage
from UI.page_model.calendar_page import CalendarPage
from UI.page_model.home_page import HomePage

driver = webdriver.Chrome('./chromedriver')
base_page = BasePage(driver)
home_page = HomePage(driver)
login_page = LoginPage(driver)
finance_page = FinancePage(driver)
day = "17"
month = "Feb"
calendar_page = CalendarPage(driver, day, month)
expected_finance_data = ['\\d+ Earnings', '\\d+ Stock splits', '\\d+ IPO pricing', '\\d+ Economic events']


def test_calendar_data():
    driver.get(home_page.url)
    driver.maximize_window()

    if base_page.consent_form.is_displayed():
        base_page.accept_button.click()

    base_page.sign_in_button.click()

    login_username = WebDriverWait(driver, timeout=3).until(lambda x: login_page.username_field)
    login_username.send_keys(username)
    login_page.sign_in_button.click()

    login_password = WebDriverWait(driver, timeout=3).until(lambda x: login_page.password_field)
    login_password.send_keys(password)
    login_page.sign_in_button.click()

    # financial part: go to Finance page
    finance_tab = WebDriverWait(driver, timeout=3).until(lambda x: base_page.finance_tab)
    finance_tab.click()
    # hover over market tab and select calendar option in popup panel
    action = ActionChains(driver)
    market_data_tab = WebDriverWait(driver, timeout=3).until(lambda x: finance_page.market_data_tab)
    action.move_to_element(market_data_tab).perform()
    action.move_to_element(finance_page.calendar_option).click().perform()

    # check calendar options
    WebDriverWait(driver, timeout=3).until(lambda x: calendar_page.calendar_form)

    calendar_page.prev_date_button.click()
    WebDriverWait(driver, timeout=3).until(lambda x: calendar_page.get_specific_day_locator())
    actual_finance_data = calendar_page.get_day_market_data()

    # since parameters for data are constantly changing, it's better to use regular expression to check the data
    for i in range(len(expected_finance_data)):
        assert re.match(expected_finance_data[i], actual_finance_data[i].text)

    driver.quit()
