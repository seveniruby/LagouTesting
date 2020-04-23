from test_app.page.main import MainPage


class TestSearch:
    def setup(self):
        self.search_page = MainPage().search()

    def test_search(self):
        assert self.search_page.search("alibaba").get_price() > 100

    def teardown(self):
        self.search_page.close()
