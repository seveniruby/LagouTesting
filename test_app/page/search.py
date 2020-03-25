from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, keyword):
        self.find_element(By.ID, "search_input_text").send_keys(keyword)
        self.click(By.ID, 'name')
        return self

    def get_price(self):
        return float(self.find_element(By.ID, 'current_price').text)

    def select(self):
        self.click(By.ID, "follow_btn")
        return self

    def cancel(self):
        self.click(By.ID, "action_close")

    def close(self):
        self.driver.quit()
