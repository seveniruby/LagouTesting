import pytest

from test_frameworks.demo import fun


def test_fun():
    assert fun(2, 1) == 2
    assert fun(2, 1) == 1


class TestFun:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def test_fun_1(self):
        assert fun(2, 1) == 2

    def test_fun_2(self):
        assert fun(2, 1) == 1

    @pytest.mark.parametrize("first, second, expect", [
        (2, 1, 2),
        (10, 2, 5),
        (10, 5, 2)
    ])
    def test_params(self, first, second, expect):
        assert fun(first, second) == expect

    def teardown_method(self):
        print("teardown_method")
