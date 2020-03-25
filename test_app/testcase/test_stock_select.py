import pytest

from test_app.page.main import MainPage


class TestStockSelect:
    @classmethod
    def setup_class(cls):
        cls.stock_select_page = MainPage().stock_select()
        cls.stock_select_page.clear_all()

    @pytest.mark.parametrize("name, code", [
        ("拼多多", "pdd"),
        ("阿里巴巴", "alibaba"),
        ("京东", "jd"),
        ("中国平安", "pingan"),
    ])
    def test_add_stock(self, name, code):
        assert name in self.stock_select_page.select(code).get_stocks()
