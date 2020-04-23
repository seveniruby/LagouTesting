from test_web.page.main import Main


class TestSearch:
    def setup(self):
        self.search_page = Main().search("selenium")

    def test_search(self):
        authors = self.search_page.search_by(author="Wayyt", keyword="selenium").get_authors()
        assert len(authors) > 0
        for result in authors:
            assert result == 'Wayyt'
