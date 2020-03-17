from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_frameworks.base_page import BasePage
from test_frameworks.search_page import SearchPage


class MainPage(BasePage):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")

    def search(self, keyword):
        element_input=self.find(By.NAME, 'q')
        element_input.clear()
        element_input.send_keys(keyword)
        element_input.send_keys(Keys.ENTER)
        return SearchPage(self.driver)
