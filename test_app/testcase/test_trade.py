from test_app.page.main import MainPage


class TestTrade:
    @classmethod
    def setup_class(cls):
        cls.trade_page = MainPage().trade()

    def test_a_gu(self):
        self.trade_page.market_a().open_account("15600534760", "1234")

    def teardown(self):
        self.trade_page.close()
