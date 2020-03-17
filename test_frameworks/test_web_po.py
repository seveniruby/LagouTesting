import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_frameworks.main_page import MainPage
from test_frameworks.search_page import SearchPage


class TestWeb:
    main_page: MainPage = None

    # @classmethod
    # def setup_class(cls):
    #     cls.main_page = MainPage()
    #
    def setup_method(self):
        self.main_page = MainPage()

    def test_search_by_po_sogo(self):
        assert self.main_page.search("sogo").get_name() == "搜狗"

    def test_search_by_po_alibaba(self):
        assert self.main_page.search("alibaba").get_name() == "阿里巴巴"

    @pytest.mark.parametrize("keyword, name", yaml.safe_load(open("test_frameworks/demo.yaml")))
    def test_search_by_po_dd(self, keyword, name):
        assert self.main_page.search(keyword).get_name() == name

    @pytest.mark.parametrize("keyword, name", [
        ("pdd", "拼多多"),
        ("xiaomi", "小米"),
        ("jd", "京东")
    ])
    def test_search_by_po_dd_yaml(self, keyword, name):
        assert self.main_page.search(keyword).get_name() == name

    def teardown_method(self):
        self.main_page.close()
