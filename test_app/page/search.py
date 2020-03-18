from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        self.driver: WebDriver =driver

    def search(self, keyword):
        self.find_element(By.ID, "search_input_text").send_keys(keyword)
        self.find_element(By.ID, 'name').click()
        return self

    def get_price(self):
        return float(self.find_element(By.ID, 'current_price').text)

    def close(self):
        self.driver.quit()
