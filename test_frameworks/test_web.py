from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_frameworks.main_page import MainPage
from test_frameworks.search_page import SearchPage


class TestWeb:
    main_page: SearchPage = None

    def test_search(self):
        driver = webdriver.Chrome()
        driver.get("https://xueqiu.com/")
        driver.find_element(By.NAME, 'q').send_keys("sogo")
        driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
        assert driver.find_element(By.CSS_SELECTOR, '.search__stock__bd span').text == "搜狗"

    @classmethod
    def setup_class(cls):
        cls.main_page = MainPage()

    def test_search_by_po_sogo(self):
        assert self.main_page.search("sogo").get_name() == "搜狗"

    def test_search_by_po_alibaba(self):
        assert self.main_page.search("alibaba").get_name() == "阿里巴巴"
