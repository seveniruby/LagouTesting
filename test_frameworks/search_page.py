from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from test_frameworks.base_page import BasePage


class SearchPage(BasePage):

    def get_name(self):
        return self.find(By.CSS_SELECTOR, '.search__stock__bd span').text

    def search(self, keyword):
        element_input=self.find(By.NAME, 'q')
        #todo: clear不生效
        element_input.clear()
        print(element_input.text)
        element_input.send_keys(keyword)
        element_input.send_keys(Keys.ENTER)
        return self
