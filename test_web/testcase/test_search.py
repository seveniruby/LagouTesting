import pytest

from test_web.page.main import Main


class TestSearch:
    def setup_class(self):
        self.main=Main()
        self.search_page = self.main.search("selenium")

    @pytest.mark.parametrize("name", ["Wayyt", "seveniruby", "Hogwarts-Ashin"])
    def test_search(self, name):
        authors = self.search_page.search_by(author=name, keyword="selenium").get_authors()
        assert len(authors) > 0
        for result in authors:
            assert result == name

    def teardown_class(self):
        self.main.quit()
